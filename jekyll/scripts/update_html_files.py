#!/usr/bin/env python3
"""
Script to update all HTML files in the docs directory to include navigation JavaScript
and remove inline styles that have been moved to the CSS file.
"""

import os
import re
from pathlib import Path

def update_html_file(file_path):
    """Update a single HTML file to include navigation JavaScript and remove inline styles."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the file already has the script tag
        if '<script src="/assets/js/navigation.js"></script>' in content:
            print(f"Skipping {file_path} - already updated")
            return
        
        # Remove the inline style block
        style_pattern = r'<!-- BDIRKS include style sheet from docs here -->\s*<!-- This should be moved to css -->\s*<style>\s*\.container\s*\{\s*display:\s*flex;\s*/\* Use flexbox layout \*/\s*\}\s*\.sidebar\s*\{\s*flex:\s*0\s*0\s*20%;\s*/\* Set the initial and minimum width of the sidebar to 20% \*/\s*background-color:\s*lightgray;\s*margin-right:\s*0\.5em;\s*margin-top:\s*1em;\s*\}\s*\.content\s*\{\s*flex:\s*1;\s*/\* Fill the remaining space with the main content \*/\s*background-color:\s*white;\s*\}\s*</style>'
        content = re.sub(style_pattern, '', content, flags=re.DOTALL)
        
        # Add the script tag after the CSS link
        css_link_pattern = r'(<link rel="stylesheet" href="/assets/css/styles\.css">)'
        replacement = r'\1\n    <script src="/assets/js/navigation.js"></script>'
        content = re.sub(css_link_pattern, replacement, content)
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {file_path}")
        
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

def main():
    """Update all HTML files in the docs directory."""
    docs_dir = Path(__file__).parent
    
    # Find all HTML files
    html_files = list(docs_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to update")
    
    for html_file in html_files:
        update_html_file(html_file)
    
    print("Update complete!")

if __name__ == "__main__":
    main() 