import struct
from random import Random 
''' Generate a Data file 
    byte byte byte 20char 20char byte byte byte
'''
r=Random()
bfile=open('data.bin','wb')
for i in range(100):
    x=i%255
    y=x+1%255
    z=y+1%255
    tx=(str(99340000+r.randint(1,99999))+' '*20)[0:20]
    rx=(str(99340000+r.randint(1,99999))+' '*20)[0:20]
    print("%d %d %d %s %s %d %d %d"%(x,y,z,tx,rx,x,y,z))
    bfile.write(struct.pack('b b b 20s 20s b b b',x,y,z,tx,rx,x,y,z))
    bfile.write('\n')
bfile.close()
