#!/bin/bash

# start the server
cd /home/martin/FACES_SINA/quest
./run.py &

# wait till it is presumably running
sleep 4

# show the site in firefox
/usr/bin/firefox -new-window http://127.0.0.1:5000/
