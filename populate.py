import csv
import os
import sys
import shutil
import argparse
import re
from datetime import datetime

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = str(value).lower()
    value = re.sub(r'[^\w\s-]', '', value)
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--slug', type=str, help='Generate for a single lead by slug')
    args = parser.parse_args()

    template_path = 'template.html'
    csv_path = 'leads.csv'

    if not os.path.exists(template_path):
        print(f"Error: {template_path} not found.")
        sys.exit(1)

    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        sys.exit(1)

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    success_count = 0

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Assume headers map directly to placeholders.
            # Handle slug logic. Check if CSV has a 'SLUG' column, else generate from BUSINESS_NAME
            slug = row.get('SLUG') or (slugify(row.get('BUSINESS_NAME', '')) if row.get('BUSINESS_NAME') else None)
            
            if not slug:
                continue
                
            if args.slug and slug != args.slug:
                continue

            # Create lead directory
            lead_dir = os.path.join(output_dir, slug)
            os.makedirs(lead_dir, exist_ok=True)

            content = template_content

            # Replace placeholders
            for key, value in row.items():
                if key:  # Ensure key is not None
                    placeholder = f"{{{{{key}}}}}"
                    content = content.replace(placeholder, str(value).strip() if value else "")

            # Default replacements as requested
            content = content.replace("{{YEAR}}", str(datetime.now().year))
            
            # If SERVICE_4 is empty or not in row
            service_4 = row.get('SERVICE_4', '').strip()
            if not service_4:
                content = content.replace("{{SERVICE_4}}", "Coming Soon")

            # Write index.html
            output_file_path = os.path.join(lead_dir, 'index.html')
            with open(output_file_path, 'w', encoding='utf-8') as out_f:
                out_f.write(content)

            success_count += 1

    print(f"Generated {success_count} sites successfully")

if __name__ == "__main__":
    main()
