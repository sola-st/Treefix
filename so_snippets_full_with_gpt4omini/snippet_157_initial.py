# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
from l3.Runtime import _l_
filehandle = open("text.txt", "w")
_l_(399)
filebuffer = ["hi","welcome","yes yes welcome"]
_l_(400)
filehandle.writelines(filebuffer)
_l_(401)
filehandle.close()
_l_(402)

