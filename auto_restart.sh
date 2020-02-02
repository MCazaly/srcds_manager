#!/bin/bash
set -e
cd "$(dirname "$0")"

source env/bin/activate
hash python3

python3 auto_restart.py
