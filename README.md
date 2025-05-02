# 🌱 MicroPython SHT11 Temperature & Humidity Sensor

This project demonstrates how to interface the **SHT11 sensor** with a **MicroPython-compatible ESP32 board (e.g., Lolin32 Lite)** to measure **temperature** and **relative humidity**. It uses **bit-banged communication** and is written fully in MicroPython.

---

## 📁 Project Structure

```
MicroPython-SHT11
├── LICENSE                    # License file (e.g., MIT)
├── README.md                  # This documentation
└── project/
    ├── main.py                # Main script to read and display sensor values
    └── sht11.py               # SHT11 driver implementation in MicroPython
```

---

## 📦 Requirements

* ⚙️ **MicroPython board**: Tested on Lolin32 Lite (ESP32)
* 🌡️ **Sensor**: Sensirion SHT11 (Digital Temp & RH sensor)
* 🧠 **Firmware**: MicroPython 1.20 or later
* 🧰 **Development tools**:

  * [Thonny IDE](https://thonny.org/) or [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html)
  * USB to Serial connection

---

## 🔌 Wiring

| SHT11 Pin | Description  | ESP32 Pin (Example) |
| --------- | ------------ | ------------------- |
| 1 (SCK)   | Clock        | GPIO 26             |
| 2 (DATA)  | Data         | GPIO 33             |
| 3 (GND)   | Ground       | GND                 |
| 4 (VCC)   | Power (3.3V) | 3.3V                |

> ⚠️ Note: Do **not** power SHT11 with 5V — it's a 3.3V device.

---

## 🧪 Example Usage

In the `main.py`:

```python
# example code to read SHT11 using MicroPython
# author : Ardy Seto P
# email  : 2black0@gmail.com
# board  : Lolin32 Lite (ESP32)

from sht11 import SHT11

# Define SCK and DATA GPIO pins
sht = SHT11(sck=26, data=33)

# Read temperature and humidity
tempOut = sht.temperature()
humOut = sht.humidity()

# Display results
print('Temperature: ', tempOut, '*C')
print('Humidity: ', humOut, '%')
```

---

## 🔧 Features of the `SHT11` Driver

* 📡 Pure MicroPython bit-banged protocol (no I2C)
* 📊 Reads:

  * Temperature (°C)
  * Relative Humidity (%RH)
* ✅ Includes:

  * CRC check
  * Command protocol implementation
  * Adjustable temperature compensation for RH

### Key Methods

```python
SHT11(sck, data)         # Initialize driver with SCK and DATA pins
.temperature()           # Return temperature in °C
.humidity(temp=25)       # Return relative humidity (%), with temp compensation
.read_register()         # Read status register (raw access)
```

---

## ⚙️ Advanced Notes

* This driver replicates the SHT11 protocol using direct GPIO pin manipulation.
* Built-in CRC-8 validation helps detect communication errors.
* The `.humidity()` method includes temperature compensation if called with custom temperature values.

---

## 💡 Troubleshooting

* ❌ **CRC or ACK errors**: Make sure your wires are short and well-connected. SHT11 is sensitive to interference.
* 🔁 **Slow reads?** SHT11 has \~200–300 ms measurement latency; this is normal.
* 📉 **Values look wrong?** Double-check power source and resistor pull-up configuration (if needed).

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## 👤 Author

**Ardy Seto Priambodo**
✉️ [2black0@gmail.com](mailto:2black0@gmail.com)