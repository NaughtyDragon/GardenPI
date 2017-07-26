#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install python-pip python-dev python-rpi.gpio 

pip install flask
