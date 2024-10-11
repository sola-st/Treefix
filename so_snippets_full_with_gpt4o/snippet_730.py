# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
from l3.Runtime import _l_
try:
    import glob
    _l_(11977)

except ImportError:
    pass
try:
    import re
    _l_(11979)

except ImportError:
    pass

mapfile = input("Enter map file name with extension eg. codifica.txt: ")
_l_(11980)
sep = input("Enter map file column separator eg. |: ")
_l_(11981)
mask = input("Enter search mask with extension eg. 2010*txt for all files to be processed: ")
_l_(11982)
suff = input("Enter suffix with extension eg. _NEW.txt for newly generated files: ")
_l_(11983)

rep = {} # creation of empy dictionary
_l_(11984) # creation of empy dictionary

with open(mapfile) as temprep:
    _l_(11988)

    for line in temprep:
        _l_(11987)

        (key, val) = line.strip('\n').split(sep)
        _l_(11985)
        rep[key] = val
        _l_(11986)

for filename in glob.iglob(mask):
    _l_(11996)


    with open (filename, "r") as textfile:
        _l_(11995)

        text = textfile.read()
        _l_(11989)

        # start replacement
        #rep = dict((re.escape(k), v) for k, v in rep.items()) commented to enable the use in the mapping of re reserved characters
        pattern = re.compile("|".join(rep.keys()))
        _l_(11990)
        text = pattern.sub(lambda m: rep[m.group(0)], text)
        _l_(11991)

        #write of te output files with the prompted suffice
        target = open(filename[:-4]+"_NEW.txt", "w")
        _l_(11992)
        target.write(text)
        _l_(11993)
        target.close()
        _l_(11994)

