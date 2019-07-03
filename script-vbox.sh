#!/bin/sh

base_image="kali.ova"

vboxmanage natnetwork add --netname NatNetwork --network "192.168.15.0/24" --enable --dhcp on

vboxmanage import ${base_image}

vboxmanage snapshot Kali-Linux-2019.2-vbox-amd64 take skali
vboxmanage clonevm Kali-Linux-2019.2-vbox-amd64 --name clone1 --options link --snapshot skali --register
vboxmanage modifyvm clone1 --nic1 natnetwork
vboxmanage modifyvm clone1 --usbohci off --usbehci off --usbxhci off


vboxmanage snapshot Kali-Linux-2019.2-vbox-amd64 take skali
vboxmanage clonevm Kali-Linux-2019.2-vbox-amd64 --name clone2 --options link --snapshot skali --register
vboxmanage modifyvm clone2 --nic1 natnetwork
vboxmanage modifyvm clone2 --usbohci off --usbehci off --usbxhci off
