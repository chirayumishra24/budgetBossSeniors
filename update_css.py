import os, glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '/* Heading Responsiveness */' not in content:
        injection = '''
    /* Heading Responsiveness */
    @media (min-width: 1024px) {
        .header-bg h2, .header-bg h1 {
            font-size: 3.2rem !important;
        }
        .topic h3, .text-3xl {
            font-size: 2.8rem !important;
            line-height: 1.3 !important;
        }
    }
    @media (min-width: 769px) and (max-width: 1023px) {
        .header-bg h2, .header-bg h1 {
            font-size: 2.5rem !important;
        }
        .topic h3, .text-3xl {
            font-size: 2.2rem !important;
            line-height: 1.3 !important;
        }
    }
'''
        content = content.replace('</style>', injection + '</style>')
        
    if f == '1.1.html':
        mobile_css = """        .evolution-timeline {
            flex-direction: column;
            gap: 1.5rem;
        }"""
        mobile_css_new = """        .evolution-timeline {
            flex-direction: column;
            gap: 1.5rem;
            align-items: center;
        }"""
        content = content.replace(mobile_css, mobile_css_new)
            
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
