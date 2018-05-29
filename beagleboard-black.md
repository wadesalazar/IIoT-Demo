

Beagle Bone Black

Home: https://beagleboard.org/black

Wiki: https://elinux.org/Beagleboard:BeagleBoneBlack
https://eewiki.net/display/linuxonarm/BeagleBone+Black

Get a shell https://ofitselfso.com/BeagleNotes/HowToConnectBeagleboneBlackToTheInternetViaUSB.php

Rapid prototype via "Bonescript"
http://beagleboard.org/Support/BoneScript

Default linux dist is Debian, current verision 9.3


Cross compiler information:
https://www.linaro.org/downloads/ 
https://eewiki.net/display/linuxonarm/BeagleBone+Black#BeagleBoneBlack-ARMCrossCompiler:GCC
http://charette.no-ip.com:81/programming/2015-12-20_CrossCompiling/index.html
http://www.ti.com/product/AM3358
if older OS (Angstrom) https://datko.net/2013/05/06/cross-compiling-applications-for-the-beaglebone/
http://wind.cs.purdue.edu/doc/crosscompile.html
if rebuild dist https://github.com/TheThingSystem/steward/wiki/Bootstrapping-the-BeagleBone-Black


GPIO https://www.linux.com/learn/getting-started-beaglebone-black-1ghz-arm-linux-machine-45


## Bluetooth LE 

BT Dongle 
https://www.asus.com/us/Networking/USBBT400/

Get Bluetooth dongle running:
https://urbanjack.wordpress.com/2014/02/26/bluetooth-low-energy-ble-on-raspberry-pi-with-asus-bt-400/

Older angstrom linux guides ( some steps still apply )

https://www.cs.sfu.ca/CourseCentral/433/bfraser/other/2015-student-howtos/NXTBrickViaBlueTooth.pdf
edit connman config
https://olsonetworks.wordpress.com/2014/01/03/enabling-bluetooth-on-your-beaglebone-black/
end to end
http://www.zephyr-labs.com/?p=87

I was able to use 
apt-get install bluetooth libbluetooth-dev bluez-utils
confirm driver is present and loaded 
modprobe -v btusb
confirm Usb doggle shows up at device
lsusb
add device to bluez
echo "0b05 17cb" >> /sys/bus/usb/drivers/btusb/new_id
edit /etc/default/bluetooth
restart bluetooth 
invoke-rc.d bluetooth restart
check for device
hcitool dev
show device details
hciconfig -a





Interesting side note 
ARM Cortex-A8 processor, are enhanced with image, graphics processing, peripherals and industrial interface options such as EtherCAT and PROFIBUS. Provided we find a way to get a BBB with a MCU with the correct options this is a path to bus speed data from EtherNet/IP, PROFIBUS, PROFINET RT/IRT & SERCOS III  

