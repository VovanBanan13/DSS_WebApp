#!/bin/sh

source .envrc
source venv/bin/activate
FLASK_APP=WebApp.py
flask run --host=0.0.0.0