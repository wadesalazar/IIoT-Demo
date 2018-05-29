# Items on hand

* **Beaglebone Black** https://beagleboard.org/black. Think of this as a open source ras. pi
* **TI Sensor Tag** - http://www.ti.com/lit/ug/swru324b/swru324b.pdf
  these are little blue tooth LE dongles packed with sensors.  Great for prototyping 
  Sensor list 
  IR   Temperature   Sensor   (TMP006) http://www.ti.com/product/tmp006
  Humidity Sensor (SHT21) from Sensirion, http://www.sensirion.com/en/products/humidity
  Pressure    Sensor    (T5400)    from Epcos http://www.epcos.com/inf/57/ds/T5400.pdf
  Accelerometer (KXTJ9) from Kionix, http://www.kionix.com/accelerometers/kxtj9
  Gyroscope   (IMU 3000) from InvenSense http://www.invensense.com/mems/gyro/imu3000.html
  Magnetometer  (MAG3110)  from Freescale http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MAG3110
* **USB Bluetooth LE adapter** ( https://www.asus.com/us/Networking/USBBT400/ )

The BBB connected to the SensorTags via BLE combine nicely into what a intelligent edge device might look like.  
Serving as the local aggregator for the sensor tags 
  it is responsible for performing operations e.g. filters, routing, enriching, etc on incoming signals
  
The BBB can then pump out little bits of info or full streams 
** Max stream data density is defined by 1) bandwidth of the sensor network or 2) sensor charateristics hence all the sensor detail above


* **Multitech Conduit Gateway** with Lora card
* **Multitech mDot** prototyping board with 3 mDots
These two device allow us to simulate the limitations of working with low bandwidth high latency networks such as Lora


## Other Items
* S7-1200 Siemens PLC ( unfortunately I dont have a copy of Step 7 ) 
* Selea logic analyizer / wire protocol debugger
* 2 -1G Ethernet switchs
* 1 old 802.11 A,B wireless router 
* TS-7250 SBC https://www.embeddedarm.com/products/TS-7250 ( runs and old version of linux )





