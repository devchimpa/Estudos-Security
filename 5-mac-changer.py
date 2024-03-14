#!/usr/bin/python3

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i" , "--interface", dest="interface" , help=" Interface to change its MAC Address")
    parser.add_option("-m" , "--mac", dest="new_mac" , help=" input the  MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Por favor, insira uma interface, para mais informações use --help.")
    elif not options.new_mac:
        parser.error("[-] Por favor insira um novo mac address, para mais informações use --help.")
    return options


def change_mac(interface, new_mac):
    print(" [+] Alterando o Mac de: " + interface + " Para : " + new_mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)

ifconfig_result= supbrocess.check_output(["ifconfig" , options.interface])
print(ifconfig_result)
