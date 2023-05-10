For this project to get the code working on the raspberry pi follow these intructions https://patrikmojzis.medium.com/how-to-run-selenium-using-python-on-raspberry-pi-d3fe058f011
Guess and check the chrome driver version that works with chromium because regtular google chrome does not work on the raspberry pi without and emulataor and that is more of a hastle than guessing nd checking

also add this at the start it wont work without it dont remove it just leave it there
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--kiosk")

also if dual screens doesnt work add this to the config.txt file on the raspberry pi and go to screen configurations and activate the HMDI port that isnt working
https://support.thepihut.com/hc/en-us/articles/360015638017-Raspberry-Pi-dual-display-second-screen-not-working

also run with admin privilgages with sudo and to install package do sudo pip3 install PackageName
to run the code use sudo python3 newMain.py

to get to to grab a perticular image just change the web url to the website you want and use find by HTML tag to search for the image


#TDLR;
Set up ssh tunneling
make sure chrome driver is working
10.107.200.26 is the host ip
make sure it is the right version of chromium and chrome driver or it wont work




#follow this tutorial to setup
https://www.youtube.com/watch?v=XVvz8t3gsys

#NOTE IMPORTANT THIS IS HELPFUL
https://stackoverflow.com/questions/40121382/control-chromium-kiosk-mode-url-from-python


the frames are in the var/www/html directory
the frames are update when someone draws something then presses view on screen
the frames are named like this frame0001, frame0002, etc

#TODO find the website site and HTML layout to scrape images from
#DONE its on localhost which you can use ssh tunneling to accsess witht he raspberry pis

http://beetlejuice.local is the website where the images are hosted

---------------------------------------------
#TODO make it so that its only accsessable through ethernet 
#this stackoverflow may help https://superuser.com/questions/588067/expose-apache-server-to-local-wifi-network
#this one might be better https://stackoverflow.com/questions/5524116/accessing-localhost-xampp-from-another-computer-over-lan-network-how-to
how to make the apache web server avalible over LAN network by knowing how ti is done it is likley that we can find out how we can not do it

ok try this https://stackoverflow.com/questions/59369348/apache-2-4-allow-access-from-the-local-network-only go to this and revert it to original settings

well its accesbible by typing local host in search and beetlejuice.local

--------------------------------------------------------


make raspberry pi use subnet from the net from main PC thats connected to the PIs via ethernet cable

This may help https://raspberrypi.stackexchange.com/questions/117937/subnet-on-raspberry-pi

The easiest way is to use static IP addresses, if your device supports that. Give the device IP address 192.168.1.100 netmask 255.255.255.0 and your pi's ethernet adapter the address 192.168.1.101, same mask.

Another fairly easy way would be to buy a cheap router/switch thing with a DHCP server in it. You probably won't need gigabit speeds. This has another advantage: you can connect the "wan" interface to your home-network and allow port forwarding to the Pi. And you will probably have a few spare ports on the 192.168-lan, which can be useful.

Of course, it is also possible to set-up a DHCP server on the Pi. In that case, you can connect the device directly to Pi (no switch or cross-over cables are needed). There are plenty tutorials on how to set-up such a server (see reply by @ingo)


---------------------------------------------------
do this it has the question you want and how to do it https://stackoverflow.com/questions/64927570/how-can-i-view-a-localhost-apache-website-from-another-computer-on-the-same-netw

look at this if you are confused it is essentially ssh tuneling https://linuxize.com/post/how-to-setup-ssh-tunneling/

https://linuxize.com/post/how-to-setup-ssh-tunneling/ we probably want local port forwarding

https://serverfault.com/questions/481929/tunneling-specific-webserver-port-on-localhost-using-ssh

the link above is specific for localhost apache servers

The link below is a more through version of the link above
https://superuser.com/questions/1044260/tunneling-local-webserver-through-ssh

#this is the command to run ssh -L 3000:internalip:3000 ext.home.ip.addr

ip adress of kirta computer is 10.107.200.26

https://www.quora.com/How-do-I-access-my-Apache-server-from-another-computer

https://unix.stackexchange.com/questions/545629/unable-to-access-apache-webserver-from-local-home-network

#important https://ezunix.org/index.php?title=Set_up_Apache_server_and_SSH_client_to_allow_tunneling_SSH_over_HTTP(s)

#tutorial
https://serverfault.com/questions/229441/how-do-i-access-a-local-web-server-on-my-laptop-from-another-computer

https://stackoverflow.com/questions/9682262/how-do-i-connect-to-this-localhost-from-another-computer-on-the-same-network
