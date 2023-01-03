#!/bin/bash

# this command I use to configure my 2 monitors
xrandr --output HDMI-0 --mode 1920x1080 --pos 0x0 --dpi 96 --rate 144 --rotate left --output DP-0 --mode 1920x1080  --dpi 96 --rate 144 --pos 1080x0 --rotate normal
nitrogen --restore &
picom -b --config ~/.config/picom.conf
nm-applet &
blueman-applet &
flameshot &
dunst &
