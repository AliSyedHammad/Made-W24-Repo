!/bin/bash

# Path to the notebook
NOTEBOOK_PATH="/home/ubuntu/Made-W24-Repo/project/pipeline.ipynb"

# Convert the notebook to a Python script
jupyter nbconvert --to script "$NOTEBOOK_PATH"

python project/pipeline.py