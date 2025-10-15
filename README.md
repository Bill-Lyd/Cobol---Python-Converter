Hello Travelers team! Here I used a Cobol to Python converter to modernize old Cobol into Python.

First I asked ChatGBT to generate an example Cobol file. This file can be seen as COBOLTEST.cbl. It is a Cobol script meant to store user data.
Then I utilized some open source code I found online to convert the Cobol script. I loaded the open source zip file into my personal VS Studios, unziped, loaded COBOLTEST.cbl in its own directory, created an output directory, played around with the cobra_main.py script to make it work with COBOLTEST.cbl (Disabled EIB), and ran the code.
This generated HELLO.py, the final converted script, which I then downloaded and uploaded here.

Thank you for reading.

TLDR: Leveraged open source code, modified said code to run a batch, downloaded and uploaded results to GitHub.

Here are the console commands I ran: 
  PS C:\Users\willi\Desktop\TRAVELERS\viper-mf-main\viper-mf-main\src> python cobra_main.py ./cobol_tests/COBALTEST.cbl ./converted/
  Converting COBOL: .././cobol_tests/COBALTEST.cbl --> .././converted/
  Copybook NOT FOUND: EIB
  Aborting conversion!
  Skipping missing copybook: EIB
  completed conversion of ./cobol_tests/COBALTEST.cbl to --> ./converted/HELLO.py
