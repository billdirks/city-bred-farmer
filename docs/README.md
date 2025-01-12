# Import process

1. Upload docx file to google docs
2. export as html
3. Edit html so it only contains the <body> content.
5. Rename images inside of html file to: images/image -> images/<date> where date is like 19460507
6. Add Jekyll front matter to html page.
---
layout: default
title: May 7, 1946
---

7. Rename html file to <date>.html, eg May_7_1946.html
8. mv images dir to ./images/<date>/, eg ./images/19460507/
6. Edit _data/navigation.yml
7. `bundle exec jekyll serve` to build and spot check. `build` instead of `serve` to only build.
8. mv ./_sites to ../docs

# To do

1. add redirect to first page
2. organize html files so they don't live at top level
2. automate import process
3. self host google css and what it links out to
