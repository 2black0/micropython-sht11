# example code to read SHT11 using MicroPython
# author : Ardy Seto P
# email : 2black0@gmail.com
# web : http://robot-terbang.web.id
# board Lolin32 Lite (based on ESP32)

from sht11 import SHT11

#pin sck and data used, change with yours
sht = SHT11(sck=26, data=33)

#read temperature and humidity
tempOut = sht.temperature()
humOut = sht.humidity()

#print temperature and humidity
print('Temperature: ', tempOut, '*C')
print('Humidity: ', humOut, '%')