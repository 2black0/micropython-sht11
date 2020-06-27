# micropython-sht11

based on : https://github.com/ayoy/upython-aq-monitor

### Board Supported
Test on ESP32 (Lolin32 Lite)

### How to Use
```python
from sht11 import SHT11

#pin sck and data used, change with yours
sht = SHT11(sck=26, data=33)

#read temperature and humidity
tempOut = sht.temperature()
humOut = sht.humidity()

#print temperature and humidity
print('Temperature: ', tempOut, '*C')
print('Humidity: ', humOut, '%')
```