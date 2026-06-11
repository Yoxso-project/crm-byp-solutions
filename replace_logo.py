#!/usr/bin/env python3
"""Replace SVG logo with img tag using actual logo.jpg in all three HTML files."""

import re
import os

def update_talent_html():
    path = 'public/talent.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old = '''                                <a href="/" className="flex items-center space-x-2 group">
                                    <svg className="w-8 h-8 text-accent group-hover:text-white transition-all duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                    </svg>
                                    <span className="text-2xl font-bold text-white tracking-wide">ByP Solutions</span>
                                </a>'''

    new = '''                                <a href="/" className="flex items-center space-x-2 group">
                                    <img src="/img/logo.jpg" alt="ByP Solutions" className="h-8 w-auto" />
                                    <span className="text-2xl font-bold text-white tracking-wide">ByP Solutions</span>
                                </a>'''

    count = content.count(old)
    print(f"[talent.html] Match count: {count}")
    if count > 0:
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[talent.html] Updated successfully!")
    else:
        print("[talent.html] No match. Trying regex approach...")
        # Use regex to find and replace the svg + span block
        pattern = re.compile(
            r'<a href="/" className="flex items-center space-x-2 group">\s*'
            r'<svg className="w-8 h-8 text-accent[^"]*"[^>]*>\s*'
            r'<path[^/]*/>\s*'
            r'</svg>\s*'
            r'<span className="text-2xl font-bold text-white tracking-wide">ByP Solutions</span>\s*'
            r'</a>',
            re.DOTALL
        )
        match = pattern.search(content)
        if match:
            print(f"[talent.html] Regex match found at position {match.start()}")
            content = pattern.sub(new, content)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("[talent.html] Updated via regex!")
        else:
            print("[talent.html] No regex match either")


def update_form_html():
    path = 'public/form.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the form.html SVG logo block
    old_pattern = re.compile(
        r'<svg className="w-8 h-8 text-brand-600"[^>]*>\s*'
        r'<path[^/]*/>\s*'
        r'</svg>',
        re.DOTALL
    )

    match = old_pattern.search(content)
    if match:
        print(f"[form.html] SVG match found at position {match.start()}")
        replacement = '<img src="/img/logo.jpg" alt="ByP Solutions" className="h-8 w-auto" />'
        content = old_pattern.sub(replacement, content, count=1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("[form.html] Updated!")
    else:
        print("[form.html] No SVG match found")


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    update_talent_html()
    update_form_html()

    # Final verification
    for f in ['index.html', 'public/talent.html', 'public/form.html']:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
        print(f"\n=== {f} ===")
        print(f"  logo.jpg references: {c.count('img/logo.jpg')}")
        print(f"  Old SVG shield (M9 12l2 2) count: {c.count('M9 12l2 2 4-4m5.618')}")
