# Import process

Relevant scripts: `download_email.py`, `generate_ingest_cmds.py`, `ingest_docx.py`, `run.sh`.

This should be more automated but but here is the current process:

1. Download emails attachments using `download_email.py`.
1. Open `generate_ingest_cmds.py`. Edit the top 2 variables `path` and `files`.
2. Run `generate_ingest_cmds.py` to generate the ingest commands. Copy and paste this output to `run.sh`.
3. Run `run.sh` to ingest the files.
4. `bundle exec jekyll serve` to build and spot check. `build` instead of `serve` to only build.
5. mv ./_sites to ../docs
    * Before doing the `mv` the .py and .sh files and the README.md file should be deleted from the _sites directory.

# To do

1. organize html files so they don't live at top level
