# ardu-sentop-linux-system
This project show temperature, memory and percentage of used info in your Linux/GNU system. 
![ardu-sentop](./pictures/ardu-sentop.JPG)

## Hardware Parts ##

* PCD8544/5110 LCD
* Arduino UNO 

## Connections ##
![ardu-sentop-circuit](./pictures/schematic.jpg)

Arduino UNO|PCD8544/Nokia 5110 |Description
-----------|-----------|-------------------------------------------------------------
GND        |GND        |Ground
3V         |VCC        |3.3V
 3         |CLK        |Output from Arduino SPI clock
 4         |DIN        |Output from Arduino SPI MOSI to display data input
 5         |D/C        |Output from display data/command to Arduino
 6         |CE         |Output from Arduino to chip select/enable display
 7         |RST        |Output from Arduino to reset display

## Dependencies ##
* Linux/GNU Operating System.
* [Arduino IDE v. 1.6.7]
  (https://www.arduino.cc/en/Main/Software).
* [Adafruit-GFX-Library]
  (https://github.com/adafruit/Adafruit-GFX-Library).
* [Adafruit-PCD8544-Nokia-5110-LCD-library]
  (https://github.com/adafruit/Adafruit-PCD8544-Nokia-5110-LCD-library).
* [psutil]
  (https://github.com/giampaolo/psutil).
* [pysensors]
  (https://github.com/bastienleonard/pysensors).


## Credit ##
This project is based on [ardutop] (https://github.com/ecardoz/ardutop). The difference between these two projects is that in ardu-sentop-linux-system, you can read mem data in GB instead MB, for those who have more than 9 GB RAM this is very useful. Addionality, I've add some additional code to read sensors values from lm sensors using pysensors module. 
