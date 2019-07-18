#Mise en place d'un r�seau simple de machines virtuelles VirtualBox

##Pr�requis

* Installer le logiciel VirtualBox ([https://www.virtualbox.org](https://www.virtualbox.org)).

* T�l�charger l'image contenant l'installation du syst�me en la
  t�l�chargeant depuis l'URL suivante:
  [https://mybox.inria.fr/d/491056058b/](https://mybox.inria.fr/d/491056058b/). L'archive
  contenant l'image s'appelle *kali.tgz*

* T�l�charger le script python de configuration qui est disponible [ici](vbox.py). Le nom du script est *vbox.py*

## Description

Nous allons configurer VirtualBox de telle sorte qu'on puisse lancer n
machines virtuelles qui sont toutes dans un r�seau local
(192.168.15.0/24) et qui auront acc�s � internet via la machine
h�te. Afin d'�viter de gaspiller de l'espace de stockage inutillement,
nous allons utiliser une seule image et dire � VirtualBox de ne
stocker que les modifications apport�es � chacune des machines: Nos
machines seront � la base des cl�nes qui pourront se diff�rencier si
besoin est. La topologie du r�seau virtuel obtenu correspond � la
figure ci-dessous:

![](figures/vboxnet.png)

##Mise en place

* �diter le script vbox.py pour d�finir les variables vdi (chemin
  d'acc�s � l'image sur la machine h�te) et vboxpath (r�pertoire
  d'installation de VirtualBox). vboxpath n'a besoin d'�tre d�finie
  que sur des machines h�tes windows.

* Lancer le script python vbox.py

Apr�s l'ex�cution du script vbox.py, VirtualBox est a priori
correctement configur�. Il faut alors lancer le programme
VirtualBox. Vous devrez alors obtenir un affichage tel que celui ci:

![](figures/install.png)

Il suffit alors de d�marrer les machines virtuelles appel�es *clone0*,
*clone1*, etc. Pour ce faire, il suffit de double-cliquer sur chacune
des machines. Une fois cette �tape effectu�e, il y aura autant de
nouvelles fen�tres que de machines virtuelle. Le r�sultat devrait
ressembler � ceci:

![](figures/run.png)

##Remarques

* Le nombre de machines virtuelles est d�fini par la variable *nvm* dans
  le script python

* Les cl�nes sont configur�s de telle sorte que les modifications
  apport�es � chaque machine virtuelle sont perdues lorsque celle-ci
  est etteinte (i.e. les images sont r�initialis�es � chaque
  red�marrage). Pour activer la conservation des modifications, il
  faut:
    * Ouvrir le gestionnaire de m�dias virtuels pour trouver le nom du
       disque associ� � la machine virtuelle pour laquelle la
       persistance doit �tre activ�e
![](figures/persist.png)

    * Il s'ag�t maintenant de noter l'UUID du disque qui correspond �
       notre machine (27c8cd04-617c-49bb-bbc7-ffe5751448ad dans notre
       exemple).    
    * Enfin, il faut utiliser l'utilitaire VboxManage (en ligne de
       commande) pour activer la persistance:
    
sous linux
    root@machine# VBoxManage modifyhd 27c8cd04-617c-49bb-bbc7-ffe5751448ad --autoreset off
sous windows:
    C:\> cd Program Files\Oracle\VirtualBox
    C:\Program Files\Oracle\VirtualBox> VBoxManage modifyhd 27c8cd04-617c-49bb-bbc7-ffe5751448ad --autoreset off

* Pour supprimer les machines virtuelles qui on �t� ajout�es, il
suffit de les s�lectionner et d'utiliser le clic droit et s�lectionner
supprimer (il est n�cessaire de tout supprimer tous les fichiers). Il
est n�cessaire aussi de supprimer les r�seau virtuel qui a �t� cr��
pour faire communiquer les machines virtuelles. Pour ce faire, il faut
cliquer sur param�tres et s�lectionner r�seau. Ensuite il faut
supprimer le r�seau monreseau:

![](figures/remove.png)
