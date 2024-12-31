#!/bin/bash
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install poetry
poetry install

echo "Virtual environment setup complete. Activate using: source venv/bin/activate"