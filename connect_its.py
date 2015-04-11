#!/usr/bin/env python
__author__ = 'avs'

import subprocess

#subprocess.call(["ls", "-l"])

sudo = 'sudo'
pon = 'pon'
pon_arg = "its"
print("Open pptp session")

#subprocess.call([sudo, pon, pon_arg])

subprocess.call("sudo pon its", shell=True)
subprocess.call("sleep 7", shell=True)
print("Add default route to ppp0")
subprocess.call("sudo ip route add 192.168.49.0/24 dev ppp0", shell=True)
subprocess.call("sleep 3", shell=True)
print("Establish rdesktop connection")
subprocess.call("rdesktop 192.168.49.2 -g 1280x1024", shell=True)
