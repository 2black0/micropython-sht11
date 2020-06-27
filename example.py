# example code to read SHT11 using MicroPython
# author : Ardy Seto P
# email : 2black0@gmail.com
# web : http://robot-terbang.web.id
# board Lolin32 Lite (based on ESP32)

from sht1x import SHT1X

#pin sck and data used, change with yours
sht11 = SHT1X(sck=26, data=33)

#read temperature and humidity
tempOut = sht11.temperature()
humOut = sht11.humidity()

#print temperature and humidity
print('Temperature: ', tempOut, '*C')
print('Humidity: ', humOut, '%')