#!/bin/bash

# Create and activate the virtual environment
python3 -m venv myenvwlc
source myenvwlc/bin/activate

# Install requirements
pip3 install -r requirements.txt

# Run the app
python3 app.py

# Deactivate the virtual environment when you're done
deactivate

