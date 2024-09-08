#!/bin/bash

HOSTNAME=$(hostnamectl hostname)

if [ "$HOSTNAME" == "aero" ]; then
    feh --bg-center .dotfiles/i3/wp.jpg .dotfiles/i3/brs.jpg
elif [ "$HOSTNAME" == "zero" ]; then
    xwinwrap -g 1920x1080+3840 -ov -ni -s -nf -- mpv --speed=0.5 --loop --wid=%WID special_shapes.mkv
fi
