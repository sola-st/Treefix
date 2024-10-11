# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
from l3.Runtime import _l_
myfile = open("data.txt","r")
_l_(14530)
data = ""
_l_(14531)
lines = myfile.readlines()
_l_(14532)
for line in lines:
    _l_(14534)

    data = data + line.strip();
    _l_(14533)

