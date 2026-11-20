# Hardware Overview

MachineVaidya is built around a compact sensor‑attachment that plugs onto the motor or driven equipment.  The following components constitute the current **Bill of Materials (estimated)** and their primary functions.

| Component | Approx. cost (₹) | Function |
|---|---|---|
| **ESP32‑DevKitC** | 300 | 802.11 b/g/n Wi‑Fi, MCU (160 MHz), GPIO, ADC – runs DSP and streams features.
| **ADXL345 3‑axis accelerometer** | 150 | Measures vibration and shock; outputs ±16 g range via I²C.
| **INMP441 MEMS microphone** | 120 | Captures acoustic signature of the machine; I²S digital output.
| **ACS712 current sensor (5 A or 20 A)** | 100 | Senses motor current draw; provides analog voltage proportional to RMS current.
| **DS18B20 digital temperature sensor** | 80 | Provides point temperature of motor housing or bearings.
| **Miscellaneous** (wires, prototype PCB, enclosure, connectors) | ~150 | Physical integration, power distribution, protection.
| **Total (estimate)** | **≈ ₹ 1 000** | – |
> The numbers are indicative; a detailed BOM will be finalised during **Phase 1**.

## Wiring diagram (high‑level)
```
[Power source] --> 3.3 V regulator --> ESP32

ESP32 GPIO14 (I²C SDA) <---> ADXL345 SDA
ESP32 GPIO13 (I²C SCL) <---> ADXL345 SCL

ESP32 GPIO27 (I²S WS) <---> INMP441 WS
ESP32 GPIO26 (I²S CLK) <---> INMP441 BCLK
ESP32 GPIO25 (I²S DATA) <---> INMP441 DIN

ESP32 GPIO34 (ADC) <---> ACS712 Vout

ESP32 GPIO32 (1‑Wire) <---> DS18B20 DATA (with pull‑up resistor)
```
*All sensors operate at 3.3 V supplied by the ESP32 regulator.  The ESP32 samples each sensor at appropriate rates (e.g., 1 kHz for accelerometer, 44.1 kHz for microphone) and computes short‑time FFTs and statistical descriptors locally before sending the feature vector over Wi‑Fi to the companion device.*

## Enclosure & mounting
* A 3‑D‑printed or laser‑cut housing clips onto the motor shaft or bearing housing.
* Sensor orientation:
  * Accelerometer – axis aligned with vibration direction.
  * Microphone – aperture facing away from motor to capture acoustic emission.
  * Current sensor – placed on motor supply line.
* Ensure secure grounding and protect against dust/moisture for field deployments.

---

**Future hardware extensions** (planned for later phases)
* **BLE module** for direct smartphone connectivity.
* **SD card** for extended local logging.
* **Battery pack** for fully untethered operation.
* **Additional sensors** – e.g., humidity, RPM tachometer.

---

*All hardware specifications are provisional and subject to change based on testing outcomes.*

