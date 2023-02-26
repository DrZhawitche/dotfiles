#!/bin/sh

uptime=$(uptime --pretty| cut -c 3-)
set $uptime=uptime:inutes=%
echo $uptime
