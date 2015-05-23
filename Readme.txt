Barakat,
        I hope that you are well. This is about Binary Writing and Reading in Python.

 I am sorry that I was not abke to answer your question about exactly what was in the data files before I left for holiday. However I hope that the supplied link will do that.

  There are two python files Gen.py and Read.py....


Gen.py
  This generates data. It should produce 100 Records, and place them in a file called  data.bin.


Read.py
  This reads the file called data.bin, and prints the data (in 2 ways) to the screen.

Data.bin
  This is a binary data file - it has 8 fields. 6 Fields are byte fields, 2 fields are 20 character number like fields.

  The data is written in the format
   byte byte byte string string byte byte byte NEW_LINE

  Each record is 47 bytes long

You can verify that the file has been generated correctly by using a hexdump command or ghex.

Assuming that you can follow my coding - you should be able to knock up a quick test script for the 2 "Oribo" type data files.

The O-HELL format is much nastier but if you follow the decode process and look at the XML output... you can see if the data you want is in this file.




