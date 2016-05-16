#!/bin/bash

sudo chmod 777 /dev/vchiq

cd ~/record/
#./mjpg_streamer -i "./input_raspicam.so -y -r 320*240 -fps 2" -o "./output_http.so -w ./www" 
./mjpg_streamer -i "./input_raspicam.so -x 320 -y 240" -o "./output_http.so -w ./www" 
