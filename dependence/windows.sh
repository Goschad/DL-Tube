#!/bin/sh

# install all dependance

echo "launch install all dependance ...\n"
sudo apt-get install python3-pip
python.exe -m pip install --upgrade pip
pip install os
pip install pytube
pip install colorama