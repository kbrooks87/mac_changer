import subprocess

interface = raw_input("interface >")
new_mac = raw_input("new Mac address >")

print("[+] Change MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + "down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + "up", shell=True)
subprocess.call("ifconfig", shell=True)