# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
from l3.Runtime import _l_
filehandle = open("text.txt", "w")
_l_(11893)
filebuffer = ["hi","welcome","yes yes welcome"]
_l_(11894)
filehandle.writelines(filebuffer)
_l_(11895)
filehandle.close()
_l_(11896)

