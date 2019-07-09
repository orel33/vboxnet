#!/usr/bin/python
import os
import subprocess

vdi="/tmp/kali.vdi"

vboxpath=""
vboxmanage=vboxpath+"VBoxManage"

#number of Virtual Machines to be created
nvm=2


cmd=vboxmanage+" modifyhd "+vdi+" --type immutable"
print(cmd)
subprocess.call([vboxmanage,"modifyhd",vdi,"--type","immutable",])
#os.system(cmd)


#configure the NAT network
cmd=vboxmanage+" natnetwork add --netname mynatnetwork --network  \"192.168.15.0/24\" --enable --dhcp on"
print(cmd)
subprocess.call([vboxmanage,"natnetwork","add","--netname","mynatnetwork","--network","\"192.168.15.0/24\"","--enable","--dhcp","on"])
#os.system(cmd)

for x in range(nvm):

    #add and configure a VM whose name is clone<x>
    name="clone"+str(x)
    
    cmd=vboxmanage+" createvm --name \""+name+"\" --ostype Debian_64 --register"
    print(cmd)
    subprocess.call([vboxmanage,"createvm","--name",name,"--ostype","Debian_64","--register"])
    #os.system(cmd)

    cmd=vboxmanage+" storagectl \""+name+"\" --name \"sata1\" --add sata"
    print(cmd)
    subprocess.call([vboxmanage,"storagectl",name,"--name","sata1","--add","sata"])
    #os.system(cmd)

    cmd=vboxmanage+" storageattach \""+name+"\" --storagectl \"sata1\" --port 0 --device 0 --type hdd --medium "+vdi
    print(cmd)
    subprocess.call([vboxmanage,"storageattach",name,"--storagectl","sata1","--port","0","--device","0","--type","hdd","--medium",vdi])
    #os.system(cmd)

    cmd=vboxmanage+" modifyvm "+name+" --nic1 mynatnetwork"
    subprocess.call([vboxmanage,"modifyvm",name,"--nic1","natnetwork","--nat-network1","mynatnetwork"])
    print(cmd)
    #os.system(cmd)

    cmd=vboxmanage+" modifyvm "+name+" --usbohci off --usbehci off --usbxhci off"
    print(cmd)
    subprocess.call([vboxmanage,"modifyvm",name,"--usbohci","off","--usbehci","off","--usbxhci","off"])
    #os.system(cmd)

    cmd=vboxmanage+" modifyvm "+name+" --memory 2048"
    print(cmd)
    subprocess.call([vboxmanage,"modifyvm",name,"--memory","2048"])
    #os.system(cmd)

    cmd=vboxmanage+" modifyvm "+name+" --vram 128"
    print(cmd)
    subprocess.call([vboxmanage,"modifyvm",name,"--vram","128"])
    #os.system(cmd)
