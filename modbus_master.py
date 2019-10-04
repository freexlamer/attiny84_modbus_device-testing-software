#!/usr/bin/env python3
import minimalmodbus
import time
import random

slave_id = 0x10
slave_baudrate = 9600
serial_port = '/dev/ttyUSB0'

instrumentA = minimalmodbus.Instrument(serial_port, slave_id)
instrumentA.serial.baudrate = slave_baudrate
instrumentA.serial.timeout = 1
instrumentA.mode = minimalmodbus.MODE_RTU

print('M90E26')
print(instrumentA.read_register(1, 1))
print(instrumentA.read_register(2, 1))
print(instrumentA.read_register(3, 1))
instrumentA.write_register(3, 7531, functioncode=6)
print(instrumentA.read_register(3, 1))


print('relays')
print(instrumentA.read_register(128, 1))
print(instrumentA.read_register(129, 1))


print('ds18b20')
print(instrumentA.read_register(132, 1))
print(instrumentA.read_register(133, 1))



print('relays')

for i in range(5):
    instrumentA.write_register(128, random.randint(0,1), functioncode=6)
    instrumentA.write_register(129, random.randint(0,1), functioncode=6)
    time.sleep(0.2)
    print('{} {}'.format(instrumentA.read_register(128, 1),instrumentA.read_register(129, 1)))

instrumentA.write_register(128, 0, functioncode=6)
instrumentA.write_register(129, 0, functioncode=6)


