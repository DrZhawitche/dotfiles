#!/bin/bash
DEPLIST="`sed -e 's/#.*$//' -e '/^$/d' software.txt | tr '\n' ' '`"
emerge --autounmask-continue -q $DEPLIST
