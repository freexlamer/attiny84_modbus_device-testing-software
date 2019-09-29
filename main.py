#!/usr/bin/env python3
import minimalmodbus
import time
import random

slave_id = 0x10
slave_baudrate = 9600

instrumentA = minimalmodbus.Instrument('/dev/ttyUSB0', slave_id)
instrumentA.serial.baudrate = slave_baudrate
instrumentA.serial.timeout = 0.2
instrumentA.mode = minimalmodbus.MODE_RTU


print(instrumentA.read_register(1, 1))
#time.sleep(0.005)


print(instrumentA.read_register(128, 1))
#time.sleep(0.005)

print(instrumentA.read_register(132, 1))
#time.sleep(0.005)

instrumentA.write_register(1, 2, functioncode=6)

for i in range(50):
    instrumentA.write_register(128, random.randint(0,3), functioncode=6)
    time.sleep(0.2)
    print(instrumentA.read_register(128, 1))

instrumentA.write_register(128, 0, functioncode=6)

#print(instrumentA.write_register(1, 2, functioncode=16))


