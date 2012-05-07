@echo off
C:\Python32\python.exe C:\Users\Bogdan\git\HID\webcam\webcam.py
C:\Python26\python.exe C:\Users\Bogdan\git\HID\ImageDifference\cropper.py
C:\Python26\python.exe C:\Users\Bogdan\git\HID\ImageDifference\imgdif.py
echo %ERRORLEVEL%
if %ERRORLEVEL% == 5 goto Bogdan
if %ERRORLEVEL% == 7 goto Mihai
if %ERRORLEVEL% == 0 goto None
:Bogdan
C:\Python25\python.exe C:\Users\Bogdan\git\HID\Mihai\Bogdan.py
goto:eof
:Mihai
C:\Python25\python.exe C:\Users\Bogdan\git\HID\Mihai\Mihai.py
goto:eof
:None
C:\Python25\python.exe C:\Users\Bogdan\git\HID\Mihai\two.py
goto:eof