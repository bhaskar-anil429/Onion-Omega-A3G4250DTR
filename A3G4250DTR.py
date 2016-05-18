# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# A3G4250DTR
# This code is designed to work with the A3G4250DTR_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

from OmegaExpansion import onionI2C
import time
import sys

print 'Starting: onionI2C module testing...'

i2c     = onionI2C.OnionI2C(0)

# set the verbosity
i2c.setVerbosity(1)

# A3G4250DTR address, 0x68(104)
# Select control register1, 0x20(32)
#               0x0F(15)        Output Data rate = 100Hz, Power ON, X , Y, Z-Axis enabled
value = [0x0F]
val     = i2c.writeBytes(0x68, 0x20, value)
print '   writeBytes returned: ', val
# A3G4250DTR address, 0x68(104)
# Select control register4, 0x23(35)
#               0x00(00)        Data LSB @ lower address, Self test disabled
value = [0x00]
val     = i2c.writeBytes(0x68, 0x23, value)
print '   writeBytes returned: ', val
time.sleep(0.5)

# A3G4250DTR address, 0x68(104)
# Read data back from 0x28(40), 2 bytes
# X-Axis LSB, X-Axis MSB
data0 = i2c.readBytes(0x68, 0x28,1)
data0 = map(str,data0)
data0 = ''.join(data0)
data0 = int(data0)
data1 = i2c.readBytes(0x68, 0x29,1)
data1 = map(str,data1)
data1 = ''.join(data1)
data1 = int(data1)

# Convert the data
xGyro = data1 * 256 + data0
time.sleep(0.5)
#if xGyro > 32767 :
#       xGyro == 65536
# A3G4250DTR address, 0x68(104)
# Read data back from 0x2A(42), 2 bytes
# Y-Axis LSB, Y-Axis MSB
data0 = i2c.readBytes(0x68, 0x2A,1)
data0 = map(str,data0)
data0 = ''.join(data0)
data0 = int(data0)
data1 = i2c.readBytes(0x68, 0x2B,1)
data1 = map(str,data1)
data1 = ''.join(data1)
data1 = int(data1)
# Convert the data
yGyro = data1 * 256 + data0
time.sleep(0.5)
#if yGyro > 32767 :
#       yGyro == 65536

# A3G4250DTR address, 0x68(104)
# Read data back from 0x2C(44), 2 bytes
# Z-Axis LSB, Z-Axis MSB
data0 = i2c.readBytes(0x68, 0x2C,1)
data0 = map(str,data0)
data0 = ''.join(data0)
data0 = int(data0)
data1 = i2c.readBytes(0x68, 0x2D,1)
data1 = map(str,data1)
data1 = ''.join(data1)
data1 = int(data1)

# Convert the data
zGyro = data1 * 256 + data0
time.sleep(0.5)
#if zGyro > 32767 :
#       zGyro == 65536
print ' \n ' 
# Output data to screen
print "X-Axis of Rotation : %d" %xGyro
print "Y-Axis of Rotation : %d" %yGyro
print "Z-Axis of Rotation : %d" %zGyro
time.sleep(0.5)

