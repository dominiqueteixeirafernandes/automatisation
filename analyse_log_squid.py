#!/usr/bin/env python3

import re

liste2=[]
liste3=["\n"]

with open("/var/log/squid/access.log", "r") as file:
    for ligne in file:

        url=re.findall(r'(CONNECT |https?://)([-\w\.]+(:\d+)?)',ligne) # recherche format regex d'une url
        heure=re.findall(r"../Mar/2019:..:..",ligne)                   # recherche format regex du mois en cours

        if url!=[]:
            for i in url:    # boucle sur liste 'url' 
                if i[1] not in liste2:    # test de présence d'élément nouveau
                    liste2+=[i[1]]+heure+liste3 # ajout à liste2 d'un nouvel élément + heure + retour ligne(\n)
    print("\n\nListe sites visités au mois de mars : ")
    print("\n")
    print(" ".join(liste2))


