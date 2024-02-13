#!/usr/bin/python3
# neste trecho são importadas as libs subprocess para comando no sistema e optparse para argumentos e opções em linha de comando.
import subprocess
import optparse
# esta função define quais são as opções aceitas e retorna os argumentos
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i" , "--interface", dest="interface" , help=" Interface to change its MAC Address")
    parser.add_option("-m" , "--mac", dest="new_mac" , help=" input the  MAC Address")
    return parser.parse_args()

# esta função utiliza a lib subprocess para executar os comandos Linux.
def change_mac(interface, new_mac):
    print(" [+] Alterando o Mac de: " + interface + " Para : " + new_mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# A função get_arguments recebe o retorno de options e arguments
(options, arguments) = get_arguments()
# e repassa esse retorno para options.interface e options.mac
change_mac(options.interface, options.new_mac)
