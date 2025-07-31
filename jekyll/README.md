# Import process

Relevant scripts: `download_email.py`, `generate_ingest_cmds.py`, `ingest_docx.py`, `run.sh`, `update_html_files.py`.

This should be more automated but but here is the current process:

1. Download emails attachments using `download_email.py`.
1. Open `generate_ingest_cmds.py`. Edit the top 2 variables `path` and `files`.
2. Run `generate_ingest_cmds.py` to generate the ingest commands. Copy and paste this output to `run.sh`.
3. Run `run.sh` to ingest the files.
4. `bundle exec jekyll serve` to build and spot check. `build` instead of `serve` to only build.
5. mv files from ./_sites to ../docs
    * Before doing the `mv` the .py and .sh files and the README.md file should be deleted from the _sites directory.
    * To get the navigation bar to scroll we do some post processing to the produced outputs using `update_html_files.py`
    * There is custom css and js to handle the sidebar. They already exist in docs/ and should be preserved. They are in `docs/` at: `/assets/js/navigation.js` and `/assets/css/styles.css`.
        
6. To serve the files from docs:
```
cd docs && python3 -m http.server 8080 --bind 127.0.0.1
```

# To do

1. organize html files so they don't live at top level
