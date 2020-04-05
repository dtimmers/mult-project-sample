#!/bin/bash

# install necessary packages for pypi server
pip install pypiserver==1.3.2
pip install passlib==1.7.2

# start pypi server
pypi-server -p 8081 -P .htaccess packages/