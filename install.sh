#!/bin/bash
set -e

cd "$(dirname "$0")"
hash python3
hash pip3

echo "Installing virtualenv..."
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
echo "Installing requirements..."
python3 -m pip install -r requirements.txt

echo "Installation complete!"