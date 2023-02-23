#!/bin/sh

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom -b &
volumeicon &
/usr/bin/emacs --daemon &
nitrogen --restore
