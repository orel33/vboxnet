#!/usr/bin/python
import os

VDI="/tmp/kali.vdi"

vboxmanage="VBoxManage"

nvm=2

cmd="chmod a+r "+VDI
print (cmd)
os.system(cmd)

cmd=vboxmanage+" modifyhd "+VDI+" --type immutable"
print(cmd)
os.system(cmd)


#network
cmd=vboxmanage+" natnetwork add --netname mynatnetwork --network  \"192.168.15.0/24\" --enable --dhcp on"
print(cmd)
os.system(cmd)

for x in range(nvm):

    name="clone"+str(x)
    
    cmd=vboxmanage+" createvm --name \""+name+"\" --ostype Debian_64 --register"
    print(cmd)
    os.system(cmd)

    cmd=vboxmanage+" storagectl \""+name+"\" --name \"sata1\" --add sata"
    print(cmd)
    os.system(cmd)

    cmd=vboxmanage+" storageattach \""+name+"\" --storagectl \"sata1\" --port 0 --device 0 --type hdd --medium "+VDI
    print(cmd)
    os.system(cmd)


    cmd=vboxmanage+" modifyvm "+name+" --nic1 mynatnetwork"
    print(cmd)
    os.system(cmd)



    cmd=vboxmanage+" modifyvm "+name+" --usbohci off --usbehci off --usbxhci off"
    print(cmd)
    os.system(cmd)

    cmd=vboxmanage+" modifyvm "+name+" --memory 2048"
    print(cmd)
    os.system(cmd)

    cmd=vboxmanage+" modifyvm "+name+" --vram 128"
    print(cmd)
    os.system(cmd)


# vboxmanage modifyvm clone1 --memory 2048
# vboxmanage modifyvm clone2 --memory 2048

