#!/usr/bin/env python3


from subprocess import call
import os.path

#######
# Création d'une ou plusieurs machines virtuelles type Debian/64 avec 2Go de mémoire, 10Go de disque dur
# Avec une interface NAT...
#######

nb=int(input("Combien de machines à installer ? : "))
for i in range(nb):
   
    nomMach=input("Indiquer le nom de la machine Linux n°" + str(i+1) +": " )
    cheminVDI='C:\\Users\\DP\\VirtualBox" "VMs/'
    chem=os.path.join(cheminVDI, nomMach)
    chemin=os.path.join(chem, nomMach)


    call("VBoxManage createvm  --name " + nomMach + " --register ")

    call("VBoxManage modifyvm  " + nomMach + " --memory 2048 --ostype Debian_64 ")
    call("VBoxManage modifyvm  " + nomMach + " --vram 128 ")

    call("VBoxManage createmedium --filename " + chemin + " --size 10000 --format VDI ")

    call("VBoxManage storagectl " + nomMach + " --name IDE --add ide --controller PIIX4 ")
    call("VBoxManage storageattach " + nomMach + " --storagectl IDE --port 0 --device 0 --type dvddrive --medium C:\\Users\DP\Downloads\debian-9.8.0-amd64-DVD-1.iso")
    call("VBoxManage storagectl " + nomMach + " --name SATA --add sata --controller IntelAhci")
    call("VBoxManage storageattach " + nomMach + " --storagectl SATA --port 0 --device 0 --type hdd --medium " + chemin + ".vdi" )

    call("VBoxManage modifyvm " + nomMach + " --usb on --usbehci on --mouse usbtablet --draganddrop bidirectional --audioout on ")

    call("VBoxManage modifyvm " + nomMach + " --nic1 nat --nictype1 82540EM --ioapic on --clipboard bidirectional ")
    print(chemin)
    
    dem=input("Voulez-vous la démarrer ?(o/n)")
    if dem=="o" or dem=="O":
        call("VBoxManage startvm " +nomMach + " --type gui")
        
#######
# Création d'un clone d'une machine installée : deb1
#######
ch=input("Souhaitez-vous créer un clone d'une machine Linux ? (o/n)")
if ch=="o" or ch=="O":
    nom=input("Nom de la machine ? :")
    cheminVDI='C:\\Users\\DP\\VirtualBox" "VMs/'
    clone=os.path.join(cheminVDI, "deb1")
    clone2=os.path.join(clone, "deb1.vdi")
    dest=os.path.join(cheminVDI, nom)
    dest2=os.path.join(dest, nom)
    dest3=".".join([dest2, "vdi"])
    print(dest3)
    call("VBoxManage clonemedium " + clone2  + " " + dest3  + " --format VDI " )
         




















      
