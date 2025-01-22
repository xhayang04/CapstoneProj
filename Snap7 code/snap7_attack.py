#----------------------------- Connect PLC ------------------------------#
import snap7
import struct

plc = snap7.client.Client()
plc.connect('10.6.1.111', 0, 1)  # IP address, rack, slot
#print(plc.get_connected())

#-------------------------------- Body ----------------------------------#
db_number = 1
start_offset = 4
bit_offset = 0
value = 0 

start_address = 154
lenght = 2

def writeBool(db_number, start_offset, bit_offset, value):
    reading = plc.db.read(db_number, start_offset, 1)
    snap7.util.set_bool(reading, 0, bit_offset, value)
    plc.db_write(db_number, start_offset, reading)
    return None

def readBool(db_number, start_offset, bit_offset):
    reading = plc.db_read(db_number, start_offset, 1)
    a = snap7.util.get_bool(reading, 0, bit_offset)
    print('DB Number: ' + str(db_number) + ' Bit ' + str(start_offset) + '.' + str(bit_offset))
    return None

def readMemory(start_address, lenght):
    reading = plc.read_area(snap7.type.Areas.MK, 0, start_address, lenght)
    value = struct.unpack('>h', reading)
    print('Start Address: ' + str(start_address) + ' Value: ' + str(value))

def writeMemory(start_address, lenght, value):
    plc.mb_write(start_address, lenght, bytearray(struct.pack('>h', value)))
    print('Start Address: ' + str(start_address) + ' Value: ' + str(value))


#------------------------------- Output ---------------------------------#
writeBool(db_number, start_offset, bit_offset, value)
readBool(db_number, start_offset, bit_offset)

writeMemory(start_address, lenght, -15000)
readMemory(start_address, lenght)