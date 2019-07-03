#!/bin/sh

VDI="/tmp/kali.vdi"


chmod a+r $VDI

vboxmanage modifyhd $VDI --type immutable

vboxmanage createvm --name "clone1" --ostype Debian_64 --register
vboxmanage createvm --name "clone2" --ostype Debian_64 --register

vboxmanage storagectl "clone1" --name "sata1" --add sata
vboxmanage storagectl "clone2" --name "sata1" --add sata

vboxmanage storageattach "clone1" --storagectl "sata1" --port 0 --device 0 --type hdd --medium $VDI
vboxmanage storageattach "clone2" --storagectl "sata1" --port 0 --device 0 --type hdd --medium $VDI

vboxmanage natnetwork add --netname NatNetwork --network "192.168.15.0/24" --enable --dhcp on

vboxmanage modifyvm clone1 --nic1 natnetwork
vboxmanage modifyvm clone1 --usbohci off --usbehci off --usbxhci off
vboxmanage modifyvm clone2 --nic1 natnetwork
vboxmanage modifyvm clone2 --usbohci off --usbehci off --usbxhci off

vboxmanage modifyvm clone1 --memory 2048
vboxmanage modifyvm clone2 --memory 2048

#vboxmanage modifyhd Your-Disk-Id-In_Here --autoreset off

