# IIoT-Demo
bits for connecting the odds and ends in my garage

## Lora network

Lora background https://lora-alliance.org/


Multitech Conduit gateway with Lora card

2 multitech mDot Lora nodes with development board 
ASUS wireless USB adapter 

MDots --- --- Gateway ------ Internet ------- HDP 

At a really high level what we have is a gateway radio that can tx/rx with mDots which are just mini radios with a MCU on board  

The gateway bridges two networks in this case the 900MHz frequency over-the-air network called Lora with a ethernet based networks composed of the devices connected to our unmanaged switch 

The gateway is a Linux based device interacted with via a SSH session  

( if necessary there is also a debug terminal ) 

More info about accessing a SSH session can be found here:  

http://www.multitech.net/developer/software/mlinux/getting-started-with-conduit-mlinux/ 

 

If you need to adapt the Linux distro being used on the gateway … 

You have the ability to modify, customized the distribution, tool chain etc 

https://www.yoctoproject.org/docs/2.5/brief-yoctoprojectqs/brief-yoctoprojectqs.html 

 

I believe the pre baked version is limited to these packages  
https://openwrt.org/packages/index/start 

 

Once we have a session and generally configured the gateway we need to get our Lora network server ( the software that will periodically wake up and check to see what clients are waiting to transmit )  

It is also time to configure the mDot devices that will be our simulated client device.  

Both of these steps are available here 
http://www.multitech.net/developer/software/lora/getting-started-with-lora-conduit-mlinux/ 

The complete command reference for the mDots can be found here  
http://www.multitech.com/documents/publications/manuals/s000643.pdf 

Connecting details here  
http://www.multitech.net/developer/software/mdot-software/mdot-connecting-to-a-network/ 

 
The provided hello world example can be viewed via reading data from the mosquitto queue  
http://www.multitech.net/developer/software/lora/conduit-mlinux-lora-communication/ 

( Mosquitto is a MQTT implementaiton )  

We will have minify query the MQTT queue to access data   

First we will need to build minify on our host or cross compile for mLinux  
The tool chain for building is available here  
http://www.multitech.net/developer/software/mlinux/mlinux-software-development/mlinux-c-toolchain/ 

Fun minify stuff found here  
https://github.com/apache/nifi-minifi-cpp 


We might need to adjust the make configuration though the mLinux tool chain install script should set the enviroment variables as well 
https://cmake.org/cmake/help/v3.6/manual/cmake-toolchains.7.html 
https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html 


Configure minify ConsumeMQTT processor 
https://nifi.apache.org/minifi/system-admin-guide.html 
https://github.com/apache/nifi-minifi-cpp#configuring 

MQTT -> Minify C++ -> Minify Java -> Nifi -> Phoenix 

Stretch goal … provide Serial input to mDot to transmit through data flow 

Can be done two ways  
Write our own C program or to provide a serial input to the mDot 

Example C program  

If we want to really really reach for the moon … the beagal bone can be our serial output 

