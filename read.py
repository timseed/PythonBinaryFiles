import struct
import pprint

binin=open('data.bin','rb')
try:
    while True:
       line=binin.read(47)
       print("process")
       x,y,z,tx,rx,x,y,z = struct.unpack('b b b 20s 20s b b b x',line)
       ''' Or '''
       data=struct.unpack('b b b 20s 20s b b b x',line)
       fields=('x','y','z','tx','rx','x2','y2','z2')
       d=dict(zip(fields,data))
       pprint.pprint(d)
except:
    pass
binin.close()
