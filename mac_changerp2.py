"""This is to show how python 2 can be exploited for this project
and why python 3 is better for security. when at interface input use
wlan0; ls; to see the result"""

import subprocess

interface = raw_input("interface >")
new_mac = raw_input("new Mac address >")

print("[+] Change MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + "down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + "up", shell=True)
subprocess.call("ifconfig", shell=True)
