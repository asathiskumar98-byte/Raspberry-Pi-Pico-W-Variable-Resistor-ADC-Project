# 🎛️ Raspberry Pi Pico W – Variable Resistor (ADC) Project

This project demonstrates how to read **analog values** from a **variable resistor (potentiometer)** using the **ADC (Analog-to-Digital Converter)** on the **Raspberry Pi Pico W** with **MicroPython** in **Thonny IDE**.

---

## 🧠 Concept
A **variable resistor** acts as a voltage divider.  
As you rotate its knob, the voltage at the wiper changes — the Pico’s **ADC pin** reads this as a 16-bit digital value between:

- `0` → corresponds to **0 V**
- `65535` → corresponds to **3.3 V**

---

## 🧩 Components Required
| Component | Quantity | Description |
|------------|-----------|-------------|
| Raspberry Pi Pico W | 1 | Microcontroller board |
| Variable Resistor (Potentiometer) | 1 | 10kΩ recommended |
| Jumper Wires | 3 | Male-to-Male |
| Breadboard | 1 | Optional for easy connections |

---

## ⚙️ Circuit Connection

| Potentiometer Pin | Pico W Pin | Description |
|-------------------|------------|--------------|
| 1 (VCC) | 3.3 V | Power |
| 2 (Wiper) | GPIO26 (ADC0) | Analog Signal |
| 3 (GND) | GND | Ground |

**📘 Note:**  
ADC0 = GPIO26  
ADC1 = GPIO27  
ADC2 = GPIO28  
