#!/bin/bash
set -e

# If the NordicWomenInSTEM directory doesn't exist, clone the repository
if [ ! -d "/home/jovyan/work/NordicWomenInSTEM" ]; then
    cd /home/jovyan/work
    git clone https://github.com/laumonfe/NordicWomenInSTEM.git
    echo "NordicWomenInSTEM repository cloned successfully."
fi

# Start JupyterLab without authentication for easy sharing
exec start-notebook.sh --NotebookApp.token='' --NotebookApp.password='' --ip=0.0.0.0 "$@"
