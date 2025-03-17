#!/bin/sh
set -x
echo "Hi"
export FLASK_APP=./cashman/index.py
echo "Running Flask application..."
C:/Users/teais/AppData/Local/Programs/Python/Python39/Scripts/pipenv.exe run C:/Users/teais/AppData/Local/Programs/Python/Python39/Scripts/flask.exe --debug run -h 0.0.0.0

read -p "press enter to continue"