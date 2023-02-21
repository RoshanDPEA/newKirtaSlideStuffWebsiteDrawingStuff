#follow this tutorial to setup



the frames are in the var/www/html directory
the frames are update when someone draws something then presses view on screen
the frames are named like this frame0001, frame0002, etc

#TODO find the website site and HTML layout to scrape images from


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
