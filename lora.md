#Lora network

Lora background https://lora-alliance.org/
MDots --- --- Gateway ------ Internet ------- Sink

##Multitech Conduit gateway with Lora card

At a really high level what we have is a gateway radio that can tx/rx with mDots which are just mini radios with a MCU on board

The gateway bridges two networks in this case the 900MHz frequency over-the-air network called Lora with a ethernet based networks composed of the devices connected to our unmanaged switch

* The gateway is a Linux based device interacted with via a SSH session
( if necessary there is also a debug terminal )
More info about accessing a SSH session can be found here:
http://www.multitech.net/developer/software/mlinux/getting-started-with-conduit-mlinux/

* If you need to adapt the Linux distro being used on the gateway …
You have the ability to modify, customized the distribution, tool chain etc
https://www.yoctoproject.org/docs/2.5/brief-yoctoprojectqs/brief-yoctoprojectqs.html
I believe the pre baked version is limited to these packages
https://openwrt.org/packages/index/start

* Once we have a session and generally configured the gateway we need to get our Lora network server ( the software that will periodically wake up and check to see what clients are waiting to transmit )


##Multitec mDot with prototyping board 

The mDot devices that will be our simulated client device or "thing"
mDot has no OS, mbed provides interface
The complete command reference for the mDots can be found here
http://www.multitech.com/documents/publications/manuals/s000643.pdf


##gateway + mDot "Hello world" example 
http://www.multitech.net/developer/software/lora/conduit-mlinux-lora-communication/
http://www.multitech.net/developer/software/lora/getting-started-with-lora-conduit-mlinux/
http://www.multitech.net/developer/software/mdot-software/mdot-connecting-to-a-network/


##Data generation
To provide mDot with information to to transmit through data flow

We can write a application to flash onto the mDot, put the mDot in serial mode and provide external serial data, provide the seral data through the prototype board.

###mDot Serial mode

###Prototyping board

###Custom application:
The mDot runs a firmware called mbed
Example mbed app: https://github.com/ARMmbed/mbed-os-example-lorawan


##Data collection
Use nifi to move data from device to upstream device
https://github.com/apache/nifi-minifi-cpp

MQTT -> Minify C++ -> Minify Java -> Nifi -> Sink
###On the mDot itself
The mDot is very resource limited http://www.multitech.com/documents/publications/data-sheets/86002171.pdf
Flash Memory 512 KB (400 KB customer usable) minify is small but not that small
Configure minify ConsumeMQTT processor https://nifi.apache.org/minifi/system-admin-guide.html https://github.com/apache/nifi-minifi-cpp#configuring

###On the Lora Gateway 
First we will need to build minify on our host or cross compile for mLinux
The tool chain for building is available here
http://www.multitech.net/developer/software/mlinux/mlinux-software-development/mlinux-c-toolchain/



We might need to adjust the make configuration though the mLinux tool chain install script should set the enviroment variables as well https://cmake.org/cmake/help/v3.6/manual/cmake-toolchains.7.html https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html

