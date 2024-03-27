#!/bin/bash

set -eu

export PYTHONUNBUFFERED=true

VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
  python3 -m venv $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip ]; then
  source $VIRTUALENV/bin/activate
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | python
  deactivate
fi

$VIRTUALENV/bin/pip3 install -r requirements.txt

$VIRTUALENV/bin/python3 app.py