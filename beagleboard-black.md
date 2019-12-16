

# Beagle Bone Black

Home: https://beagleboard.org/black

Wiki: https://elinux.org/Beagleboard:BeagleBoneBlack
https://eewiki.net/display/linuxonarm/BeagleBone+Black

Get a shell https://ofitselfso.com/BeagleNotes/HowToConnectBeagleboneBlackToTheInternetViaUSB.php

Rapid prototype via "Bonescript"
http://beagleboard.org/Support/BoneScript

Default linux dist is Debian, current verision 9.3

Helpful sites: 
https://www.ofitselfso.com/BeagleNotes/BeagleNotes.php
https://www.ofitselfso.com/BeagleNotes/HowToConnectBeagleboneBlackToTheInternetViaUSB.php

### Development

Cross compiler information:
* https://www.linaro.org/downloads/ 
* https://eewiki.net/display/linuxonarm/BeagleBone+Black#BeagleBoneBlack-ARMCrossCompiler:GCC
* http://charette.no-ip.com:81/programming/2015-12-20_CrossCompiling/index.html
* http://www.ti.com/product/AM3358
* if older OS (Angstrom) https://datko.net/2013/05/06/cross-compiling-applications-for-the-beaglebone/
+ http://wind.cs.purdue.edu/doc/crosscompile.html
* if rebuild dist https://github.com/TheThingSystem/steward/wiki/Bootstrapping-the-BeagleBone-Black

### Working with IO
GPIO https://www.linux.com/learn/getting-started-beaglebone-black-1ghz-arm-linux-machine-45

### Side note 
ARM Cortex-A8 processor, are enhanced with image, graphics processing, peripherals and industrial interface options such as EtherCAT and PROFIBUS. Provided we find a way to get a BBB with a MCU with the correct options this is a path to bus speed data from EtherNet/IP, PROFIBUS, PROFINET RT/IRT & SERCOS III 


## Bluetooth LE 

I found the following adapter at Fry's for ~$10 https://www.asus.com/us/Networking/USBBT400/

insert the adapter and check usb for new devices

```
lsusb
Bus 001 Device 002: ID 0b05:17cb ASUSTek Computer, Inc.
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

at first my device is not listed because the BBB i have has a broken USB host adapter.
After rebooting (several  times) with the adapter plugged in it, eventually it gets dectected 

Once the device is successfully attached via USB, load the Bluetooth driver 
```
modprobe -v btusb
```

Bluez does not recognize most USB adapters automattically so we must manually register the new device with bluez by catting the USB ID into the Bluez new_id file
```     
echo "0b05 17cb" >> /sys/bus/usb/drivers/btusb/new_id
```

There are two software packages to know 

the first, hcitool is an abstraction of the tasks the radio performs 
e.g. scan for devices, request additional informaiton from a device 

The second gatttool is an abstraction of the tasks available for BLE
e.g. read and write values read device properties 

The adapter should now be registered with Bluez and available.  Bluez enumerates each device starting at hci0, then hci1 etc
```
hcitool dev
Devices:
        hci0    5C:F3:70:8B:BE:AE
```

### Get Bluetooth dongle running
* https://urbanjack.wordpress.com/2014/02/26/bluetooth-low-energy-ble-on-raspberry-pi-with-asus-bt-400/
* https://wiki.debian.org/BluetoothUser

### Older angstrom linux guides ( some steps still apply )
* https://www.cs.sfu.ca/CourseCentral/433/bfraser/other/2015-student-howtos/NXTBrickViaBlueTooth.pdf
* https://olsonetworks.wordpress.com/2014/01/03/enabling-bluetooth-on-your-beaglebone-black/
* http://www.zephyr-labs.com/?p=87

## Reading data 

List the available devices with LE capabilities via
```
hcitool lescan
LE Scan ...
45:86:11:CB:F0:18 (unknown)
45:86:11:CB:F0:18 (unknown)
BC:6A:29:AB:2B:98 (unknown)
BC:6A:29:AB:2B:98 SensorTag
E7:18:B4:6F:37:11 (unknown)
E7:18:B4:6F:37:11 Seos
51:FF:D5:F0:DF:F3 (unknown)
```
Look for the SensorTag device and take note of the device ID 

Connect to the SensorTag device 
```
hcitool lecc BC:6A:29:AB:2B:98
```
Gatttool makes reading data easy
http://manpages.ubuntu.com/manpages/bionic/man1/gatttool.1.html

```
gatttool -b BC:6A:29:AB:2B:98 -I
[   ][BC:6A:29:AB:2B:98][LE]>
[   ][BC:6A:29:AB:2B:98][LE]> connect
[CON][BC:6A:29:AB:2B:98][LE]>
```

Gatttool can list the sensors available on the SensorTag 
We can search for content by
```
[CON][BC:6A:29:AB:2B:98][LE]> primary
attr handle: 0x0001, end grp handle: 0x000b uuid: 00001800-0000-1000-8000-00805f9b34fb
attr handle: 0x000c, end grp handle: 0x000f uuid: 00001801-0000-1000-8000-00805f9b34fb
attr handle: 0x0010, end grp handle: 0x0022 uuid: 0000180a-0000-1000-8000-00805f9b34fb
attr handle: 0x0023, end grp handle: 0x002a uuid: f000aa00-0451-4000-b000-000000000000
```

for a complete list of what these handles are can be found 
http://processors.wiki.ti.com/index.php/CC2650_SensorTag_User%27s_Guide#Gatt_Server

```
[CON][BC:6A:29:AB:2B:98][LE]> char-read-hnd 0x000b
[CON][BC:6A:29:AB:2B:98][LE]>
Characteristic value/descriptor: 50 00 a0 00 00 00 e8 03
```
writes blocked by gatttool bug in my version 

<h2>Wifi</h2>

For whatever reason the ubuntu images for BBB use connman ... I believe the main stream network manager today is NetworkManager but who is splitting hairs 

assuming your wireless adapter is up and running 
ip a 
should give an entry that looks like:

8: wlan0: <NO-CARRIER,BROADCAST,MULTICAST,DYNAMIC,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
    link/ether e0:cb:4e:a6:5b:12 brd ff:ff:ff:ff:ff:ff

Connecting to a Wifi network with connman

sudo connmanctl
connmanctl> scan wifi
connmanctl> servicesconnmanctl> services
*AO Guest                wifi_e0cb4ea65b12_4775657374_managed_psk
    ULh_Guest            wifi_e0cb4ea65b12_554c685f4775657374_managed_none
    ULh_Private          wifi_e0cb4ea65b12_554c685f50726976617465_managed_ieee8021x
    ULh_Staff            wifi_e0cb4ea65b12_554c685f5374616666_managed_psk
    Mobile               wifi_e0cb4ea65b12_4d6f62696c65_managed_psk
    ilaw                 wifi_e0cb4ea65b12_696c6177_managed_psk
    wpa2                 wifi_e0cb4ea65b12_77706132_managed_ieee8021xsf
dsfs

connmanctl> connect wifi_e0cb4ea65b12_4775657374_managed_psk
Passphrase? ****
Connected wifi_e0cb4ea65b12_4775657374_managed_psk
connmanctl> quit

now ip a should show 

8: wlan0: <BROADCAST,MULTICAST,DYNAMIC,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether e0:cb:4e:a6:5b:12 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.44/20 brd 192.168.15.255 scope global wlan0
       valid_lft forever preferred_lft forever
    inet6 fe80::e2cb:4eff:fea6:5b12/64 scope link
       valid_lft forever preferred_lft forever


Using AWS system manager to automate some tasks on the BBB 
( what security implications does this have ) ???


