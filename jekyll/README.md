# Import process

1. Run ingest.py from this directory. Here is an example:
```
python3 ./ingest_docx.py --date 19460520 --docx ../../RawDocx/CBF\ \#3_\ May\ 20,\ 1946.docx
```
2. `bundle exec jekyll serve` to build and spot check. `build` instead of `serve` to only build.
3. mv ./_sites to ../docs

# To do

1. Redo first 2 blogs with google external links
2. organize html files so they don't live at top level
