import machine
from machine import ADC
import time

variable_resistor = ADC(0)

while True:
    adc_value = variable_resistor.read_u16()
    print('step_value:',adc_value)
    time.sleep(0.2)
