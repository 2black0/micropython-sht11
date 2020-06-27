# micropython-sht11

based on : https://github.com/ayoy/upython-aq-monitor

### How to Use
```python
from sht1x import SHT1X

#pin sck and data used, change with yours
sht11 = SHT1X(sck=26, data=33)

#read temperature and humidity
tempOut = sht11.temperature()
humOut = sht11.humidity()

#print temperature and humidity
print('Temperature: ', tempOut, '*C')
print('Humidity: ', humOut, '%')
```