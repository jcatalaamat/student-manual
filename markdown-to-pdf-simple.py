#!/usr/bin/env python3
"""
Simple Markdown to PDF converter for Being Human 101 V2
Uses markdown2 and weasyprint (or falls back to simpler methods)
"""

import os
import sys

def check_and_install_packages():
    """Check if required packages are installed, offer to install if not"""
    try:
        import markdown
        print("✓ markdown package found")
    except ImportError:
        print("Installing markdown package...")
        os.system("pip3 install markdown")
        import markdown

    return markdown

def convert_md_to_html(md_file, html_file):
    """Convert markdown to HTML"""
    markdown = check_and_install_packages()

    print(f"Reading {md_file}...")
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    print("Converting to HTML...")
    html_content = markdown.markdown(md_content, extensions=['extra', 'toc', 'tables'])

    # Add CSS styling
    styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Being Human 101 - Student Manual V2</title>
    <style>
        @page {{
            margin: 1in;
            @bottom-center {{
                content: counter(page);
            }}
        }}
        body {{
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
            max-width: 8.5in;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            font-size: 24pt;
            margin-top: 30px;
            margin-bottom: 15px;
            color: #1a1a1a;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
        }}
        h2 {{
            font-size: 18pt;
            margin-top: 25px;
            margin-bottom: 12px;
            color: #2a2a2a;
        }}
        h3 {{
            font-size: 14pt;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #3a3a3a;
        }}
        h4 {{
            font-size: 12pt;
            margin-top: 15px;
            margin-bottom: 8px;
            color: #4a4a4a;
        }}
        p {{
            margin-bottom: 10px;
        }}
        ul, ol {{
            margin-bottom: 15px;
            padding-left: 30px;
        }}
        li {{
            margin-bottom: 5px;
        }}
        blockquote {{
            border-left: 4px solid #ccc;
            margin-left: 0;
            padding-left: 20px;
            color: #666;
            font-style: italic;
        }}
        code {{
            background-color: #f5f5f5;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: "Courier New", monospace;
        }}
        pre {{
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ccc;
            margin: 30px 0;
        }}
        .page-break {{
            page-break-after: always;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

    print(f"Writing HTML to {html_file}...")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(styled_html)

    print(f"✅ HTML created: {html_file}")
    return html_file

if __name__ == "__main__":
    md_file = "Being Human 101 - Student Manual V2.md"
    html_file = "Being-Human-101-Student-Manual-V2-STYLED.html"

    if not os.path.exists(md_file):
        print(f"❌ Error: {md_file} not found")
        sys.exit(1)

    html_output = convert_md_to_html(md_file, html_file)

    print("\n" + "="*60)
    print("HTML file created successfully!")
    print("="*60)
    print("\nNEXT STEPS TO CREATE PDF:")
    print("\n1. EASIEST - Open the HTML file in Chrome/Safari:")
    print(f"   open '{html_file}'")
    print("   Then: File → Print → Save as PDF")
    print("\n2. OR - Open in Safari and use Export as PDF:")
    print(f"   open -a Safari '{html_file}'")
    print("   File → Export as PDF...")
    print("\n" + "="*60)
