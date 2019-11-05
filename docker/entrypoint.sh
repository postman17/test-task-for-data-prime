#!/bin/bash

set -x

echo "Start gunicorn"

gunicorn -b 0.0.0.0:5050 app:app --timeout 1000
