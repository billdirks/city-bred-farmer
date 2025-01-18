import argparse
import datetime
import pathlib
import subprocess

JEKYLL_HTML_TEMPLATE = """---
layout: default
title: {title}
---

{contents}
"""

NAV_TEMPLATE = """- name: {name}
  link: /{link}.html
"""


def main(date: datetime.datetime, docx_path: pathlib.Path):
    # This must be run in directory where images dir lives.

    # Set shared strings
    compact_date = date.strftime("%Y%m%d")
    link_date = date.strftime("%b_%d_%Y")
    read_date = date.strftime("%b %d, %Y")
    html = f"{link_date}.html"

    # Run pandoc
    cmd = f'pandoc --extract-media images/{compact_date} -o {html} "{docx_path}"'
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

    # Add jekyll front matter to html
    with open(html, "r") as file:
        contents = file.read()

    jekyll_contents = JEKYLL_HTML_TEMPLATE.format(
        title=read_date,
        contents=contents
    )
    with open(html, "w") as file:
        file.write(jekyll_contents)

    # Update navigation
    with open("_data/navigation.yml", "a") as file:
        file.write(NAV_TEMPLATE.format(name=read_date, link=link_date))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--date', type=str, required=True, help="Format is YYYYMMDD")
    parser.add_argument('--docx', type=str, required=True, help="The docx filepath to process")
    args = parser.parse_args()
    date = datetime.datetime.strptime(args.date, "%Y%m%d")
    docx = pathlib.Path(args.docx)
    main(date, docx)

