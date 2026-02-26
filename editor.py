import re
import sys

def modify_template():
    with open('template.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Page Title & JSON-LD
    old_title = '    <title>{{BUSINESS_NAME}} | Professional Cleaning Services in {{CITY}}, {{STATE}}</title>\n    <meta name="description"\n        content="{{BUSINESS_NAME}} offers professional residential cleaning services in {{CITY}}, {{STATE}}. Trusted, insured, and locally owned. Get a free quote today!" />'
    new_title = '''    <title>Sparkle Clean Co. | Professional Cleaning in Denver, CO</title>
    <meta name="description"
        content="{{BUSINESS_NAME}} offers professional residential cleaning services in {{CITY}}, {{STATE}}. Trusted, insured, and locally owned. Get a free quote today!" />
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How much does house cleaning cost in {{CITY}}?",
          "acceptedAnswer": { "@type": "Answer", "text": "Our pricing depends on the size of your home and the type of service. Most standard residential cleanings in {{CITY}} range from $120–$250. We offer free, no-obligation quotes — just fill out the form above or give us a call." }
        },
        {
          "@type": "Question",
          "name": "How often should I schedule a cleaning?",
          "acceptedAnswer": { "@type": "Answer", "text": "Most of our {{CITY}} clients book weekly or bi-weekly for regular upkeep. We also offer monthly deep cleans for homes that need less frequent service. We'll recommend the best schedule based on your home size and lifestyle." }
        },
        {
          "@type": "Question",
          "name": "Do I need to be home during the cleaning?",
          "acceptedAnswer": { "@type": "Answer", "text": "No — most clients give us a key or door code and we handle everything while they're at work or out. Your home and belongings are fully covered by our insurance policy." }
        },
        {
          "@type": "Question",
          "name": "What's included in a standard cleaning?",
          "acceptedAnswer": { "@type": "Answer", "text": "A standard clean includes vacuuming, mopping, dusting all surfaces, cleaning bathrooms (toilets, sinks, showers), wiping down kitchen counters and appliances, and emptying trash bins. We follow a consistent checklist every visit." }
        },
        {
          "@type": "Question",
          "name": "What's the difference between regular and deep cleaning?",
          "acceptedAnswer": { "@type": "Answer", "text": "A regular clean maintains an already-clean home. A deep clean goes further — inside appliances, baseboards, window sills, grout, behind furniture, and areas often skipped in routine cleanings. We recommend a deep clean for first-time clients or homes that haven't been cleaned in a while." }
        },
        {
          "@type": "Question",
          "name": "Do you bring your own cleaning supplies?",
          "acceptedAnswer": { "@type": "Answer", "text": "Yes — we arrive fully equipped with all cleaning products and tools. If you have a preferred product or a specific allergy, just let us know and we'll accommodate." }
        },
        {
          "@type": "Question",
          "name": "Are your cleaners insured and background-checked?",
          "acceptedAnswer": { "@type": "Answer", "text": "Absolutely. Every member of our team is fully insured, bonded, and has passed a thorough background check. We take the trust you place in us seriously." }
        },
        {
          "@type": "Question",
          "name": "Do you offer eco-friendly or pet-safe cleaning products?",
          "acceptedAnswer": { "@type": "Answer", "text": "Yes. We offer eco-friendly, non-toxic cleaning options that are safe for children, pets, and people with allergies. Just mention this preference when booking and we'll bring the right products." }
        },
        {
          "@type": "Question",
          "name": "How do I prepare my home before the cleaners arrive?",
          "acceptedAnswer": { "@type": "Answer", "text": "Not much is needed — just pick up any clutter or personal items you'd like secured before we arrive. The more accessible surfaces are, the more thorough we can be. We handle the rest." }
        },
        {
          "@type": "Question",
          "name": "What areas do you serve near {{CITY}}?",
          "acceptedAnswer": { "@type": "Answer", "text": "We proudly serve {{CITY}} and surrounding areas including {{AREA_2}}, {{AREA_3}}, {{AREA_4}}, and {{AREA_5}}. Not sure if we cover your area? Give us a call and we'll let you know." }
        }
      ]
    }
    </script>'''
    content = content.replace(old_title, new_title)

    # 2. ISpark Icon
    old_ispark = '''        const ISpark = () => (
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.8} stroke="currentColor" className="w-8 h-8">
                <path strokeLinecap="round" strokeLinejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z" />
            </svg>
        );'''
    new_ispark = '''        const ISpark = () => (
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.8} stroke="currentColor" className="w-8 h-8">
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 11v8h6v-8M7 8h10M10 5v3M10 5h4v3M14 5l1-3h-6l1 3" />
            </svg>
        );'''
    content = content.replace(old_ispark, new_ispark)

    # 3. Nav Links FAQ
    old_nav_links_1 = '''            const links = [
                { label: 'Services', href: '#services' },
                { label: 'Why Us', href: '#why-us' },
                { label: 'Reviews', href: '#reviews' },
                { label: 'Contact', href: '#contact' },
            ];'''
    new_nav_links_1 = '''            const links = [
                { label: 'Services', href: '#services' },
                { label: 'Why Us', href: '#why-us' },
                { label: 'Reviews', href: '#reviews' },
                { label: 'FAQ', href: '#faq' },
                { label: 'Contact', href: '#contact' },
            ];'''
    content = content.replace(old_nav_links_1, new_nav_links_1)

    old_nav_links_2 = '''            const navLinks = [
                { label: 'Services', href: '#services' },
                { label: 'Why Us', href: '#why-us' },
                { label: 'Reviews', href: '#reviews' },
                { label: 'Contact', href: '#contact' },
            ];'''
    content = content.replace(old_nav_links_2, new_nav_links_1)

    # 4. Hero padding & Button
    old_hero = '''            <section id="hero" className="hero-bg min-h-screen flex items-center pt-16 relative" aria-label="Hero">
                <div className="max-w-6xl mx-auto px-4 sm:px-6 py-20 w-full">'''
    new_hero = '''            <section id="hero" className="hero-bg min-h-[90vh] flex items-center pt-24 pb-12 relative" aria-label="Hero">
                <div className="max-w-6xl mx-auto px-4 sm:px-6 py-10 w-full">'''
    content = content.replace(old_hero, new_hero)

    old_hero_btn = '''                            <a id="hero-quote-btn" href="#contact" className="inline-flex items-center justify-center px-7 py-4 rounded-xl text-base font-semibold text-blue-700 bg-white hover:bg-blue-50 transition shadow-lg hover:shadow-xl" onClick={e => { e.preventDefault(); scrollTo('#contact'); }}>
                                Get a Free Quote
                            </a>'''
    new_hero_btn = '''                            <a id="hero-quote-btn" href="#contact" className="inline-flex items-center justify-center px-7 py-4 rounded-xl text-base font-semibold text-white bg-blue-600 border border-transparent hover:bg-blue-700 transition shadow-lg hover:shadow-xl" onClick={e => { e.preventDefault(); scrollTo('#contact'); }}>
                                Get a Free Quote
                            </a>'''
    content = content.replace(old_hero_btn, new_hero_btn)

    # 5. More services coming soon
    old_more_sec = '<p className="text-slate-500 max-w-lg mx-auto text-base">Professional cleaning solutions for every need. More services coming soon.</p>'
    new_more_sec = '<p className="text-slate-500 max-w-lg mx-auto text-base">Professional cleaning solutions for every need.</p>'
    content = content.replace(old_more_sec, new_more_sec)

    # 6. Testimonials
    old_review_data = 'text: "I\'ve been using " + T.name + " for three months'
    new_review_data = 'text: "I\'ve been using Sparkle Clean Co. for three months'
    content = content.replace(old_review_data, new_review_data)

    # 7. Add Social Proof Bar
    hero_end_comment = '        // SECTION: HERO END'
    social_proof = '''        // SECTION: HERO END

        // ── Social Proof Bar ───────────────────────────────────────────────────
        const SocialProof = () => (
            <div className="w-full bg-slate-50 py-4 border-b border-slate-200">
                <div className="max-w-6xl mx-auto px-4 sm:px-6 flex flex-wrap justify-center items-center gap-4 text-center text-sm font-semibold text-slate-700">
                    <span>500+ Homes Cleaned</span>
                    <span className="hidden sm:inline text-slate-400">&middot;</span>
                    <span className="flex items-center gap-1"><IStar /> <span className="sr-only">4.9★</span> <span className="text-amber-500">4.9★ Average Rating</span></span>
                    <span className="hidden sm:inline text-slate-400">&middot;</span>
                    <span>100% Satisfaction Guaranteed</span>
                </div>
            </div>
        );'''
    content = content.replace(hero_end_comment, social_proof)
    
    # 8. Add FAQ Section and format components in App
    faq_section = '''        // ── FAQ ────────────────────────────────────────────────────────────────
        const FAQ = () => {
            const [openId, setOpenId] = useState(null);
            
            const faqs = [
                { id: 1, q: `How much does house cleaning cost in ${T.city}?`, a: `Our pricing depends on the size of your home and the type of service. Most standard residential cleanings in ${T.city} range from $120–$250. We offer free, no-obligation quotes — just fill out the form above or give us a call.` },
                { id: 2, q: `How often should I schedule a cleaning?`, a: `Most of our ${T.city} clients book weekly or bi-weekly for regular upkeep. We also offer monthly deep cleans for homes that need less frequent service. We'll recommend the best schedule based on your home size and lifestyle.` },
                { id: 3, q: `Do I need to be home during the cleaning?`, a: `No — most clients give us a key or door code and we handle everything while they're at work or out. Your home and belongings are fully covered by our insurance policy.` },
                { id: 4, q: `What's included in a standard cleaning?`, a: `A standard clean includes vacuuming, mopping, dusting all surfaces, cleaning bathrooms (toilets, sinks, showers), wiping down kitchen counters and appliances, and emptying trash bins. We follow a consistent checklist every visit.` },
                { id: 5, q: `What's the difference between regular and deep cleaning?`, a: `A regular clean maintains an already-clean home. A deep clean goes further — inside appliances, baseboards, window sills, grout, behind furniture, and areas often skipped in routine cleanings. We recommend a deep clean for first-time clients or homes that haven't been cleaned in a while.` },
                { id: 6, q: `Do you bring your own cleaning supplies?`, a: `Yes — we arrive fully equipped with all cleaning products and tools. If you have a preferred product or a specific allergy, just let us know and we'll accommodate.` },
                { id: 7, q: `Are your cleaners insured and background-checked?`, a: `Absolutely. Every member of our team is fully insured, bonded, and has passed a thorough background check. We take the trust you place in us seriously.` },
                { id: 8, q: `Do you offer eco-friendly or pet-safe cleaning products?`, a: `Yes. We offer eco-friendly, non-toxic cleaning options that are safe for children, pets, and people with allergies. Just mention this preference when booking and we'll bring the right products.` },
                { id: 9, q: `How do I prepare my home before the cleaners arrive?`, a: `Not much is needed — just pick up any clutter or personal items you'd like secured before we arrive. The more accessible surfaces are, the more thorough we can be. We handle the rest.` },
                { id: 10, q: `What areas do you serve near ${T.city}?`, a: `We proudly serve ${T.city} and surrounding areas including ${T.area2 || 'nearby areas'}, ${T.area3 || 'local communities'}, ${T.area4 || 'neighboring towns'}, and ${T.area5 || 'surrounding cities'}. Not sure if we cover your area? Give us a call and we'll let you know.` }
            ];

            return (
                <section id="faq" className="py-20" aria-label="FAQ">
                    <div className="max-w-4xl mx-auto px-4 sm:px-6">
                        <div className="text-center mb-14">
                            <span className="text-sm font-semibold tracking-widest uppercase" style={{ color: '#2563EB' }}>FAQ</span>
                            <h2 className="font-heading font-bold text-3xl sm:text-4xl text-slate-900 mt-2 mb-4">Frequently Asked Questions</h2>
                            <p className="text-slate-500 text-base">Everything you need to know about our cleaning services in {T.city}</p>
                        </div>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            {faqs.map(faq => (
                                <div key={faq.id} className="bg-slate-50 border border-slate-200 rounded-xl overflow-hidden h-max">
                                    <button 
                                        className="w-full text-left px-5 py-4 flex justify-between items-center bg-transparent focus:outline-none"
                                        onClick={() => setOpenId(openId === faq.id ? null : faq.id)}
                                    >
                                        <span className="font-semibold text-slate-800 pr-4">{faq.q}</span>
                                        <span className={`text-slate-400 transition-transform duration-300 ${openId === faq.id ? 'rotate-45' : ''}`}>
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M12 4.5v15m7.5-7.5h-15" /></svg>
                                        </span>
                                    </button>
                                    <div className={`px-5 pb-4 text-slate-600 text-sm leading-relaxed ${openId === faq.id ? 'block' : 'hidden'}`}>
                                        {faq.a}
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>
            );
        };
        // SECTION: FAQ END'''
    
    app_component = '''        const App = () => (
            <React.Fragment>
                <Navbar />
                <main>
                    <Hero />
                    <SocialProof />
                    <Services />
                    <WhyUs />
                    <Reviews />
                    <Contact />
                    <FAQ />
                </main>
                <Footer />
                
                {/* Mobile Sticky Bar */}
                <div className="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 p-3 z-50 flex items-center justify-between shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]">
                    <span className="text-slate-700 font-semibold text-sm">Need a clean home?</span>
                    <a href={"tel:" + T.phone} className="flex items-center gap-2 px-5 py-2.5 bg-blue-600 text-white rounded-lg font-semibold text-sm shadow-sm transition hover:bg-blue-700">
                        <IPhone /> Call Now
                    </a>
                </div>
            </React.Fragment>
        );'''
    
    content = content.replace('        const App = () => (\n            <React.Fragment>\n                <Navbar />\n                <main>\n                    <Hero />\n                    <Services />\n                    <WhyUs />\n                    <Reviews />\n                    <Contact />\n                </main>\n                <Footer />\n            </React.Fragment>\n        );', faq_section + '\n\n' + app_component)
    
    # Update Footer tag to include id
    content = content.replace('<footer className="bg-slate-900', '<footer id="footer" className="bg-slate-900')


    # 9. Merge Contact form and details!
    old_contact_section = content[content.find('        const Contact = () => {'):content.find('        // SECTION: CONTACT END')+31]
    
    new_contact_section = '''        const Contact = () => {
            const [form, setForm] = useState({ name: '', phone: '', email: '', service: '', date: '', message: '' });
            const [done, setDone] = useState(false);
            const set = e => setForm({ ...form, [e.target.name]: e.target.value });
            const submit = e => { e.preventDefault(); setDone(true); };
            const ic = "form-input w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder-slate-400 transition";

            return (
                <section id="contact" className="py-20" style={{ background: '#F8FAFC' }} aria-label="Contact">
                    <div className="max-w-6xl mx-auto px-4 sm:px-6">
                        <div className="text-center mb-14">
                            <span className="text-sm font-semibold tracking-widest uppercase" style={{ color: '#2563EB' }}>Free Quote</span>
                            <h2 className="font-heading font-bold text-3xl sm:text-4xl text-slate-900 mt-2 mb-4">Request Your Free Estimate</h2>
                            <p className="text-slate-500 max-w-lg mx-auto text-base">Fill out the form below and we'll get back to you within 24 hours.</p>
                        </div>
                        
                        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
                            {/* Left: Form */}
                            <div className="bg-white rounded-2xl shadow-sm border border-slate-100 p-8 sm:p-10">
                                <div id="ghl-form-placeholder">
                                    {done ? (
                                        <div className="text-center py-12">
                                            <div className="w-16 h-16 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-4">
                                                <svg className="w-8 h-8 text-green-600" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor">
                                                    <path strokeLinecap="round" strokeLinejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                                                </svg>
                                            </div>
                                            <h3 className="font-heading font-bold text-xl text-slate-900 mb-2">Request Received!</h3>
                                            <p className="text-slate-500">We'll reach out within 24 hours to confirm your appointment.</p>
                                        </div>
                                    ) : (
                                        <form id="quote-form" onSubmit={submit} noValidate>
                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 mb-5">
                                                <div className="sm:col-span-2">
                                                    <label htmlFor="name" className="block text-sm font-medium text-slate-700 mb-1.5">Full Name *</label>
                                                    <input id="name" name="name" type="text" required placeholder="Jane Smith" value={form.name} onChange={set} className={ic} />
                                                </div>
                                                <div>
                                                    <label htmlFor="phone" className="block text-sm font-medium text-slate-700 mb-1.5">Phone *</label>
                                                    <input id="phone" name="phone" type="tel" required placeholder="(555) 000-0000" value={form.phone} onChange={set} className={ic} />
                                                </div>
                                                <div>
                                                    <label htmlFor="email" className="block text-sm font-medium text-slate-700 mb-1.5">Email *</label>
                                                    <input id="email" name="email" type="email" required placeholder="jane@email.com" value={form.email} onChange={set} className={ic} />
                                                </div>
                                                <div>
                                                    <label htmlFor="service" className="block text-sm font-medium text-slate-700 mb-1.5">Service Type *</label>
                                                    <select id="service" name="service" required value={form.service} onChange={set} className={ic}>
                                                        <option value="">Select a service…</option>
                                                        <option value="residential">Residential Cleaning</option>
                                                        <option value="deep">Deep Cleaning</option>
                                                        <option value="move">Move-In / Move-Out Cleaning</option>
                                                        <option value="other">Other</option>
                                                    </select>
                                                </div>
                                                <div>
                                                    <label htmlFor="date" className="block text-sm font-medium text-slate-700 mb-1.5">Preferred Date</label>
                                                    <input id="date" name="date" type="date" value={form.date} onChange={set} className={ic} />
                                                </div>
                                                <div className="sm:col-span-2">
                                                    <label htmlFor="message" className="block text-sm font-medium text-slate-700 mb-1.5">Message</label>
                                                    <textarea id="message" name="message" rows={4} placeholder="Tell us about your home and any special requests…" value={form.message} onChange={set} className={ic + " resize-none"} />
                                                </div>
                                            </div>
                                            <button id="submit-quote-btn" type="submit" className="w-full py-4 rounded-xl text-base font-semibold text-white btn-primary hover:opacity-90 hover:shadow-lg transition">
                                                Request Free Quote
                                            </button>
                                        </form>
                                    )}
                                </div>
                            </div>
                            
                            {/* Right: Info */}
                            <div>
                                <span className="text-sm font-semibold tracking-widest uppercase" style={{ color: '#2563EB' }}>Contact Us</span>
                                <h2 className="font-heading font-bold text-3xl sm:text-4xl text-slate-900 mt-2 mb-4">
                                    Get In{' '}<span style={{ color: '#2563EB' }}>Touch</span>{' '}With Us
                                </h2>
                                <p className="text-slate-500 text-base leading-relaxed mb-8">
                                    Have questions or need assistance with your house cleaning needs? Our friendly team is ready to provide you with the information and support you need.
                                </p>
                                <ul className="space-y-5 mb-8">
                                    <li className="flex items-center gap-3">
                                        <span className="w-9 h-9 rounded-lg flex items-center justify-center flex-shrink-0 text-white btn-primary">
                                            <IMail />
                                        </span>
                                        <a href={'mailto:' + T.email} className="text-slate-700 hover:text-blue-600 transition text-sm font-medium">{T.email}</a>
                                    </li>
                                    <li className="flex items-center gap-3">
                                        <span className="w-9 h-9 rounded-lg flex items-center justify-center flex-shrink-0 text-white btn-primary">
                                            <IPhone />
                                        </span>
                                        <a href={'tel:' + T.phone} className="text-slate-700 hover:text-blue-600 transition text-sm font-medium">{T.phone}</a>
                                    </li>
                                    <li className="flex items-start gap-3">
                                        <span className="w-9 h-9 rounded-lg flex items-center justify-center flex-shrink-0 text-white btn-primary">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.8} stroke="currentColor" className="w-5 h-5">
                                                <path strokeLinecap="round" strokeLinejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" />
                                                <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" />
                                            </svg>
                                        </span>
                                        <span className="text-slate-700 text-sm font-medium">{T.address}</span>
                                    </li>
                                </ul>
                                
                                <div className="rounded-2xl overflow-hidden shadow-md border border-slate-100" style={{ height: '280px' }}>
                                    <iframe
                                        title="Service Area Map"
                                        src={T.mapSrc !== '{{MAP_EMBED_URL}}' ? T.mapSrc : 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.15830869428!2d-74.11976383964024!3d40.69766374874431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY!5e0!3m2!1sen!2sus!4v1708800000000!5m2!1sen!2sus'}
                                        width="100%"
                                        height="100%"
                                        style={{ border: 0 }}
                                        allowFullScreen
                                        loading="lazy"
                                        referrerPolicy="no-referrer-when-downgrade"
                                    />
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            );
        };
        // SECTION: CONTACT END'''

    content = content.replace(old_contact_section, new_contact_section)
    
    with open('template.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    modify_template()
    print("Modifications applied.")
