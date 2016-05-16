#!/bin/bash

# raspivid -t 999999 -hf -o -| socat - udp-datagram:192.168.1.102:8080 --udp-caching=500
sudo raspivid -o - -t 0 -w 640 -h 360 -fps 25|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264
