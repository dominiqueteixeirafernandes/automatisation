# automatisation

automatisation d'installation VM

1er script: create_vm.py 
>>> Création d'une machine virtuelle sous Virtualbox avec des paramètres prédéfinis (mémoire, taille disque, OS...)
-Ajout d'un fichier preseed.cfg dans l'iso (debian9_8.iso) permettant l'installation de Debian sans intervention manuelle; tous les paramettres souhaités sont inclus dans ce fichier. Le lien de ce fichier est déclaré dans 'txt.cfg'.

2ème script: main_Conf_Interfaces.py et module_Conf_Interfaces.py
>>> Ces fichiers sont à inclure dans l'iso. Ils permettent le paramétrage des interfaces réseaux. (adressage IP static ou dhcp).
Ils sont immédiatement disponibles dans un répertoire de la machine installée (/home/user/script/) et utilisables de suite avec les permissions élevées.

3ème script: analyse_log_squid.py
>>> Ce script a pour unique but d'analyser les log à travers un proxy squid d'une machine distante.











