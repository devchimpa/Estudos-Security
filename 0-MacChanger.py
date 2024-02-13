#!/usr/bin/python3

# script para alterar o endereço MAC com Python e Subprocess
import subprocess

interface = input("Interface: ")
new_mac = input("Novo Mac: ")

print(" [+] Alterando o Mac de: " + interface + " Para : " + new_mac )

subprocess.call("ifconfig " + interface + " down" , shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac , shell=True)
subprocess.call("ifconfig " + interface + " up" , shell=True)
                                                                            
