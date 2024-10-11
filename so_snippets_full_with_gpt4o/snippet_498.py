# Extracted from https://stackoverflow.com/questions/375427/a-non-blocking-read-on-a-subprocess-pipe-in-python
import os
from asyncproc import Process
myProc = Process("myprogram.app")

while True:
    # check to see if process has ended
    poll = myProc.wait(os.WNOHANG)
    if poll != None:
        break
    # print any new output
    out = myProc.read()
    if out != "":
        print out

