This is about Binary Writing and Reading in Python.

There are two python files Gen.py and Read.py....

========
Gen.py
========
  This generates data. It should produce 100 Records, and place them in a file called  data.bin.

========
Read.py
========
  This reads the file called data.bin, and prints the data (in 2 ways) to the screen.

===========
Data.bin
===========
  This is a binary data file - it has 8 fields. 6 Fields are byte fields, 2 fields are 20 character number like fields.

  The data is written in the format
   byte byte byte string string byte byte byte NEW_LINE

  Each record is 47 bytes long

You can verify that the file has been generated correctly by using a hexdump command or ghex.

