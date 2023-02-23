#!/bin/bash

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom -b &
volumeicon &
/usr/bin/emacs --daemon &
feh --bg-scale ~/.config/dwm/wallpapers/forest-fog.jpg
