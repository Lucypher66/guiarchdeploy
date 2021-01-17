from tkinter import *
import os
import paramiko
import pexpect

window = Tk()
window.title('Archdeploy')
window.geometry('1280x768')

hostname = ""
username = ""
password = ""
port = 22
command = ""
harddrive = ""
timezone = ""
format = BooleanVar()
filesystem = ""
bios = ""
uefi = ""
hostname = ""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
systemsettings = [BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar()]
newhostname = ""
newusername = ""
newpassword = ""

toinstall = [BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),]

#Keeping track how many list entries are defined
#for x in range(100):
#    print(toinstall[x])
#    print(x)

class button():
    def __init__(self,instance,width,text,command,x,y):
        self.instance = instance
        self.command = command
        self.width = width
        self.x = x
        self.y = y
        self.text = text
        Button(self.instance,width=width,height=1,command=command,text=text).place(x=x, y=y)

class label():
    def __init__(self,instance,width,height,text,x,y):
        self.instance = instance
        self.width = width
        self.height = height
        self.text = text
        self.x = x
        self.y = y
        Label(self.instance,width=width,height=height,text=text).place(x=x,y=y)

hostnamelabel = label(window,19,1,"IP-Adress/Hostname:",0,5)
hostnameentry = Entry(window,width=20,textvariable=hostname)
hostnameentry.place(x=12,y=30)

portlabel = label(window,14,1,"Port: (optional)",170,5)
portentry = Entry(window,width=20,textvariable=port)
portentry.place(x=180,y=30)

usernamelabel = label(window,11,1,"Username:",0,55)
usernameentry = Entry(window,width=20,textvariable=username)
usernameentry.place(x=12,y=80)

passwordlabel = label(window,10,1,"Password: ",170,55)
passwordentry = Entry(window,width=20,textvariable=password)
passwordentry.place(x=180,y=80)

harddrivelabel = label(window,10,1,"Hard drive:",340,5)
harddriveentry = Entry(window,width=20,textvariable=harddrive)
harddriveentry.place(x=348,y=30)

hdformatbutton = Checkbutton(window,text="Format?",variable=toinstall[15],onvalue=True,offvalue=False)
hdformatbutton.place(x=430,y=5)

desktoplabel = label(window,20,1,"Desktop Environment: ",0,180)

xfcebutton = Checkbutton(window,text="XFCE",variable=toinstall[0],onvalue=True,offvalue=False)
xfcebutton.place(x=8,y=200)

kdebutton = Checkbutton(window,text="KDE",variable=toinstall[1],onvalue=True,offvalue=False)
kdebutton.place(x=8,y=220)

lxdebutton = Checkbutton(window,text="LXDE",variable=toinstall[2],onvalue=True,offvalue=False)
lxdebutton.place(x=130,y=200)

budgiebutton = Checkbutton(window,text="Budgie",variable=toinstall[3],onvalue=True,offvalue=False)
budgiebutton.place(x=130,y=220)

gnomebutton = Checkbutton(window,text="GNOME",variable=toinstall[4],onvalue=True,offvalue=False)
gnomebutton.place(x=8,y=240)

toolslabel = label(window,7,1,"Tools:",0,280)

firefoxbutton = Checkbutton(window,text="Firefox",variable=toinstall[5],onvalue=True,offvalue=False)
firefoxbutton.place(x=8,y=300)

chromiumbutton = Checkbutton(window,text="Chromium",variable=toinstall[6],onvalue=True,offvalue=False)
chromiumbutton.place(x=130,y=300)

libreofficefreshbutton = Checkbutton(window,text="LibreOffice Fresh",variable=toinstall[7],onvalue=True,offvalue=False)
libreofficefreshbutton.place(x=130,y=320)

evolutionbutton = Checkbutton(window,text="Evolution",variable=toinstall[8],onvalue=True,offvalue=False)
evolutionbutton.place(x=8,y=320)

thunderbirdbutton = Checkbutton(window,text="Thunderbird",variable=toinstall[9],onvalue=True,offvalue=False)
thunderbirdbutton.place(x=8,y=340)

libreofficestillbutton = Checkbutton(window,text="LibreOffice Still",variable=toinstall[10],onvalue=True,offvalue=False)
libreofficestillbutton.place(x=130,y=340)

clementinebutton = Checkbutton(window,text="Clementine",variable=toinstall[11],onvalue=True,offvalue=False)
clementinebutton.place(x=8,y=360)

vlcbutton = Checkbutton(window,text="VLC",variable=toinstall[12],onvalue=True,offvalue=False)
vlcbutton.place(x=130,y=360)

loginmanagerlabel = label(window,15,1,"Login Manager:",0,400)

lightdmbutton = Checkbutton(window,text="lightdm",variable=toinstall[13],onvalue=True,offvalue=False)
lightdmbutton.place(x=8,y=420)

sddmbutton = Checkbutton(window,text="SDDM",variable=toinstall[14],onvalue=True,offvalue=False)
sddmbutton.place(x=130,y=420)

systemtoollabel = label(window,13,1,"System Tools:",5,460)

basedevelbutton = Checkbutton(window,text="base-devel",variable=toinstall[16],onvalue=True,offvalue=False)
basedevelbutton.place(x=8,y=500)

bashcompletionbutton = Checkbutton(window,text="bash-completion",variable=toinstall[17],onvalue=True,offvalue=False)
bashcompletionbutton.place(x=130,y=480)

dialogbutton = Checkbutton(window,text="dialog",variable=toinstall[18],onvalue=True,offvalue=False)
dialogbutton.place(x=130,y=500)

wpasupplicantbutton = Checkbutton(window,text="wpa_supplicant",variable=toinstall[19],onvalue=True,offvalue=False)
wpasupplicantbutton.place(x=8,y=480)

amducodebutton = Checkbutton(window,text="amd-ucode",variable=toinstall[20],onvalue=True,offvalue=False)
amducodebutton.place(x=8,y=520)

intelucodebutton = Checkbutton(window,text="intel-ucode",variable=toinstall[21],onvalue=True,offvalue=False)
intelucodebutton.place(x=130,y=520)

timezonelabel = label(window,9,1,"Timezone:",510,5)
timezoneentry = Entry(window,width=20,textvariable=timezone)
timezoneentry.place(x=516,y=30)

newhostnamelabel = label(window,15,1,"New Hostname:",670,5)
newhostnameentry = Entry(window, width=20,textvariable=newhostname)
newhostnameentry.place(x=684,y=30)

newusernamelabel = label(window,15,1,"New Username:",840,5)
newusernameentry = Entry(window,width=20,textvariable=newusername)
newusernameentry.place(x=852,y=30)

newpasswordlabel = label(window,15,1,"New Password:",1005,5)
newpasswordentry = Entry(window,width=20,textvariable=newpassword)
newpasswordentry.place(x=1020,y=30)

systemsettingslabel = label(window,17,1,"System Settings:",0,560)

legacylibsbutton = Checkbutton(window,text="32 Bit libraries",variable=systemsettings[0],onvalue=True,offvalue=False)
legacylibsbutton.place(x=8,y=580)

startbutton = button(window,10,"Start",lambda:install(),12,120)


def install():
    global format
    global newhostname
    global newpassword
    global newusername
    hostname = "192.168.5.27"#hostnameentry.get()
    username = "root"#usernameentry.get()
    port = "22"#portentry.get()
    password = "22"#passwordentry.get()
    harddrive = "/dev/sda"#harddriveentry.get()
    timezone = "Europe/Berlin"#timezoneentry.get()
    newhostname = newhostnameentry.get()
    newusername = newusernameentry.get()
    newpassword = newpasswordentry.get()




    if port == "":
        port = 22

    ssh.connect(hostname, port, username, password)
    def execute(command):
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print(lines)

    def formathdbios():
        command = "echo 'type=83' | sfdisk " + harddrive
        execute(command)


    command = "ls /"
    execute(command)
    command = "cd /"
    execute(command)
    command = "mkdir /test"
    execute(command)
    command = "ls /"
    execute(command)
    command = "rm -rf /test"
    execute(command)


    #For testing purposes
    print("Hostname/IP-Adresse: "+ hostname)
    print("Username: " + username)
    print("Port: " + port)
    print("Passwort: " + password)
    print("Festplatte: " + harddrive)
    print("Zeitzone: " + timezone)
    print("Neuer Nutzername: " + newusername)
    print("Neuer Hostname: " + newhostname)
    print("Neues Passwort: " + newpassword)
    print(toinstall[0].get())
    print(toinstall[1].get())
    print(toinstall[2].get())
    print(toinstall[3].get())
    print(toinstall[4].get())
    print(toinstall[5].get())
    print(toinstall[6].get())
    print(toinstall[7].get())
    print(toinstall[8].get())
    print(toinstall[9].get())
    print(toinstall[10].get())
    print(toinstall[11].get())
    print(toinstall[12].get())
    print(toinstall[13].get())
    print(toinstall[14].get())
    print(toinstall[15].get())
    print(toinstall[16].get())
    print(toinstall[17].get())
    print(toinstall[18].get())
    print(toinstall[19].get())
    print(toinstall[20].get())
    print(toinstall[21].get())

    if toinstall[15].get() == True:
        formathdbios()

        execute("umount " + harddrive + "1")
        mountstring = "mount " + harddrive + "1" + " /mnt"
        command = "mkfs.ext4 " + harddrive + "1"
        print(command)
        print(mountstring)
        execute(mountstring)
        execute("touch /mnt/test.txt")
    pacstrapstring = "pacstrap /mnt base linux linux-firmware acpid dbus dhcpcd nano pulseaudio pulseaudio-alsa pavucontrol networkmanager network-manager-applet cups cronie avahi "

    if toinstall[0].get() == True:
        pacstrapstring = pacstrapstring + "xfce4 xfce4-goodies "

    if toinstall[1].get() == True:
        pacstrapstring = pacstrapstring + "plasma kde-applications "

    if toinstall[2].get() == True:
        pacstrapstring = pacstrapstring + "lxde " #LXDE

    if toinstall[3].get() == True:
        pacstrapstring = pacstrapstring + "budgie-desktop gnome " #BUDGIE

    if toinstall[4].get() == True:
        pacstrapstring = pacstrapstring + "gnome gnome-extra " #GNOME

    if toinstall[5].get() == True:
        pacstrapstring = pacstrapstring + "firefox " #FIREFOX

    if toinstall[6].get() == True:
        pacstrapstring = pacstrapstring + "chromium " #CHROMIUM

    if toinstall[7].get() == True:
        pacstrapstring = pacstrapstring + "libreoffice-fresh " #LIBREOFFICE FRESH

    if toinstall[8].get() == True:
        pacstrapstring = pacstrapstring + "evolution " #EVOLUTION

    if toinstall[9].get() == True:
        pacstrapstring = pacstrapstring + "thunderbird " #THUNDERBIRD

    if toinstall[10].get() == True:
        pacstrapstring = pacstrapstring + "libreoffice-still " #LIBREOFFICE STILL

    if toinstall[11].get() == True:
        pacstrapstring = pacstrapstring + "clementine " #CLEMENTINE

    if toinstall[12].get() == True:
        pacstrapstring = pacstrapstring + "vlc " #VLC

    if toinstall[13].get() == True:
        pacstrapstring = pacstrapstring + "lightdm-gtk-greeter " #LIGHTDM

    if toinstall[14].get() == True:
        pacstrapstring = pacstrapstring + "sddm " #SDDM



    execute("genfstab -p /mnt > /mnt/etc/fstab")
    execute("cat /mnt/etc/fstab")

    if toinstall[16].get() == True:
        pacstrapstring = pacstrapstring + "base-devel "

    if toinstall[17].get() == True:
        pacstrapstring = pacstrapstring + "bash-completion "

    if toinstall[18].get() == True:
        pacstrapstring = pacstrapstring + "dialog "

    if toinstall[19].get() == True:
        pacstrapstring = pacstrapstring + "wpa_supplicant "

    if toinstall[20].get() == True:
        pacstrapstring = pacstrapstring + "amd-ucode "

    if toinstall[21].get() == True:
        pacstrapstring = pacstrapstring + "intel-ucode "

    print(pacstrapstring)
    execute(pacstrapstring)
    pacmanstring = pacmanstring + "--noconfirm"
    execute("echo ""Bis jetzt geht alles"" > /mnt/test.txt ")

    def startandenableservices():
        global toinstall
        execute("systemctl start --now NetworkManager.service && systemctl enable NetworkManager.service")
        execute("systemctl start --now cronie.service && systemctl enable cronie.service")
        execute("systemctl start --now acpid.service && systemctl enable acpid.service")
        execute("systemctl start --now avahi-daemon.service && systemctl enable avahi-daemon.service")
        execute("systemctl start --now cups.service && systemctl enable cups.service")
        execute("echo ""Dienste sind gestartet und beim Boot aktiv"" >> /mnt/test.txt ")

        if toinstall[13].get() == True:
            execute("systemctl start --now lightdm.service && systemctl enable lightdm.service")
            execute("echo ""LightDM ist gestartet und beim Boot aktiv"" >> /mnt/test.txt ")

        if toinstall[14].get() == True:
            execute("systemctl start --now sddm.service && systemctl enable sddm.service")
            execute("echo ""SDDM ist gestartet und beim Boot aktiv"" >> /mnt/test.txt ")



    if timezone == "Europe/Berlin":
        execute("rm -rf /etc/locale.gen && touch /etc/locale.gen")
        execute("echo ""de_DE.UTF-8 UTF-8"" > /etc/locale.gen")
        execute("echo ""de_DE ISO-8859-1"" >> /etc/locale.gen")
        execute("echo ""de_DE@euro ISO-8859-15"" >> /etc/locale.gen")
        execute("echo ""en_US.UTF-8"" >> /etc/locale.gen")

        execute("echo ""KEYMAP=de-latin1"" > /etc/vconsole.conf")
        execute("echo ""FONT=lat9w-16"" >> /etc/vconsole.conf")

        execute("ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime")
        execute("locale-gen")
        execute("echo ""Lokalisierungseinstellungen sind gesetzt und aktiv"" >> /mnt/test.txt ")

    execute("cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup")
    execute("sed -i 's/^#Server/Server/' /etc/pacman.d/mirrorlist.backup")
    execute("rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist")
    execute("echo ""Spiegelserver sind optimiert"" >> /mnt/test.txt ")





    execute("arch-chroot /mnt")
    print("!!!CHROOT IST AKTIV!!!")
    execute("reboot now")
window.mainloop()