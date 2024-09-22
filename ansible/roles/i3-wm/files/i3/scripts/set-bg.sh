#!/bin/bash

HOSTNAME=$(hostnamectl hostname)

if [ "$HOSTNAME" == "aero" ]; then
    feh --bg-center ~/.config/papers/wp.jpg ~/.config/papers/brs.jpg
elif [ "$HOSTNAME" == "zero" ]; then
    xwinwrap -g 1920x1080+3840 -ov -ni -s -nf -- mpv --speed=0.5 --loop --wid=%WID ~/special_shapes.mkv
fi
