!/usr/bin/python3

import subprocess

interface = input("Interface: ")
new_mac = input("Novo Mac: ")

print(" [+] Alterando o Mac de: " + interface + " Para : " + new_mac )

# melhorando o processo de armazenar a informação para evitar um Hijacking.
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
