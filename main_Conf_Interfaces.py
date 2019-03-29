#!/usr/bin/env python3
# -*- coding: utf8 -*-


import os
import sys
import module_Conf_Interfaces as mod


def main():
    c = mod.Config()
    inter = c.interfaces
    print( "\n\n\n")
    print( "Liste des interfaces : \n")
# affiche le nom des interfaces disponibles
    c.show_inter()

    enp0 = input("\nQuelle interface ?: ")
    while (enp0 not in inter):
        enp0 = input("Interface non attribuée ! Réessayez : ")
    print( "\nChoix options :")
    print( "1 : Statut configuration interface :",enp0)
    print( "2 : Définir adresse IP")
    print( "3 : Activer dhcp")

    r = input("\n> ")
    while r not in ("1","2","3"):
        print( "réessayez")
        r = input("> ")
    if r == "1":
# recherche si l'interface est défini en dhcp dans /etc/network/interfaces
        ips = c.get_ips_conf(enp0)
        if len(ips) == 0:
            print( "Interface en dhcp\n")
# affiche la configuration du fichier /etc/network/interfaces
        else:
            print( "ip      : " + c.get_ips_conf(enp0)[0])
            print( "netmask : " + c.get_ips_conf(enp0)[1])
            print( "gateway : " + c.get_ips_conf(enp0)[2])

# recherche si l'interface n'est pas défini dans /etc/network/interfaces
        if not c.test_inter(enp0):
            print( "Interface non définie !\n")

    elif r == "2":
        ip = input("ip      : ")
        nmask = input("netmask : ")
        gway = input("gateway : ")
        c.set_static_ip(enp0,ip,nmask,gway)
        print( "\nAdresse statique définie !")

    elif r == "3":
        c.enable_dhcp(enp0)
        print( "DHCP activé !")

    nouv = input("\nNouvelle configuration ('o/n') ou redémarrer ('r') pour appliquer la configuration : ")
    while nouv not in ("o","n","r"):
        print( "Réessayez !")
        nouv = input("\nNouvelle configuration ('o/n'): ou redémarrer ('r') pour appliquer la configuration :")
    if nouv.lower() == "o":
            os.system("./main_Conf_Interfaces.py")
    elif nouv.lower() == "n":
            sys.exit(0)
    else:
        os.system("reboot")

# levée d'exceptions si non root
try:
    assert os.getuid() == 0
    main()
except AssertionError:
    print( "Root obligatoire !")
    sys.exit(0)
except KeyboardInterrupt:
    print( "\nExiting...")
    sys.exit(0)


