#!/bin/bash

virtualenv .data/venv

source .data/venv/bin/activate

pip install -r requirements.txt

python app.py

deactivate
