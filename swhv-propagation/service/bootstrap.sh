#!/bin/sh

dir=~/propagation

python -m venv ${dir}
${dir}/bin/pip install --upgrade pip
${dir}/bin/pip install --upgrade .
