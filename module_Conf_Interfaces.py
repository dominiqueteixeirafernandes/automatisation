#!/usr/bin/env python3
# -*- coding: utf8 -*-


import os
import re

class Config:
    def __init__(self):
        os.system("ip -o link> /tmp/interf.txt")
        iplink_file = open("/tmp/interf.txt",'r')
        self.interfaces = re.findall(r'enp0s\d{1,2}', iplink_file.read())
        iplink_file.close()

# affiche la liste des interfaces disponibles
    def show_inter(self):
        for i in self.interfaces:
            print(i)

# test si l'interface est définie dans "/etc/network/interfaces"
    def test_inter(self,interface):
        iface_file = open("/etc/network/interfaces",'r')
        content = iface_file.read()
        cont=content.split()
        iface_file.close()

        if interface in cont:
            return True
        else:
            return False

# ajout d'une nouvelle interface
    def set_static_ip(self,interface,inet,netmask,gateway):
        if not self.test_inter(interface):
            iface_file = open("/etc/network/interfaces",'a')
            lines =["\nauto "+interface+"\n","iface "+ interface +" inet static\n","	address "+inet+"\n","	netmask "+netmask+"\n","	gateway "+gateway+"\n"]
            iface_file.writelines(lines)
            iface_file.close()

# modification d'une interface déjà présente
        else:
            iface_file = open("/etc/network/interfaces","r")
            data = iface_file.read()
            iface_file.close()
            ifaces = data.split("auto")
            for iface in ifaces:  # boucle sur liste après "auto" et indexation de la position de l'interface xx
                if interface in iface:
                    index = ifaces.index(iface)
                    ifaces.remove(iface)

            new_line = " " + interface +"\niface "+interface + " inet static\n	address "+ inet +"\n	netmask "+ netmask+"\n	gateway "+gateway
            ifaces.insert(index,new_line) # modification de la ligne concernée par l'interface xx
            new_data = "auto".join(c for c in ifaces)
            iface_file2 = open("/etc/network/interfaces","w")
            iface_file2.write(new_data)
            iface_file2.close()

# récupération de la configuration de l'interface
    def get_ips_conf(self,interface):
        if self.test_inter(interface):
            iface_file = open("/etc/network/interfaces","r")
            content = iface_file.read()
            iface_file.close()
            ips_list = re.findall(r'\d+\.\d+\.\d+\.\d+',content)
            return ips_list
        else:
            return []

# modification des paramètres static --> dhcp
    def enable_dhcp(self,interface):
        if self.test_inter(interface):
            iface_file = open("/etc/network/interfaces","r")
            data = iface_file.read()
            iface_file.close()
            ifaces = data.split("auto")
            for enp0 in ifaces:
                if interface in enp0:
                    index = ifaces.index(enp0)
                    ifaces.remove(enp0)
                    new_line = " " + interface +"\niface "+interface + " inet dhcp\n"
                    ifaces.insert(index,new_line)

                    new_content = "auto".join(i for i in ifaces)
                    iface_file2 = open("/etc/network/interfaces","w")
                    iface_file2.write(new_content)
                    iface_file2.close()

# définit les paramètres en dhcp
        else:
            new_line = "auto "+interface +"\niface "+interface + " inet dhcp\n"
            iface_file2 = open("/etc/network/interfaces","a")
            iface_file2.write(new_line)
            iface_file2.close()


