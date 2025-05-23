#!/bin/bash
set -e

# Always clone fresh
cd /home/jovyan/work
rm -rf NordicWomenInSTEM
git clone https://github.com/laumonfe/NordicWomenInSTEM.git
echo "NordicWomenInSTEM repository cloned freshly."

# Start JupyterLab without authentication for easy sharing
exec start-notebook.sh --NotebookApp.token='' --NotebookApp.password='' --ip=0.0.0.0 "$@"
