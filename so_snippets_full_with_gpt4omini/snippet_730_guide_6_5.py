import glob # pragma: no cover
import re # pragma: no cover

mapfile = 'codifica.txt' # pragma: no cover
sep = '|' # pragma: no cover
mask = '2010*.txt' # pragma: no cover
suff = '_NEW.txt' # pragma: no cover
rep = {'apple': 'fruit', 'banana': 'yellow fruit'} # pragma: no cover
with open(mapfile, 'w') as f: f.write('apple|fruit\nbanana|yellow fruit\n') # pragma: no cover
with open('2010_example.txt', 'w') as f: f.write('This text contains apple and banana for replacement.') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string
from l3.Runtime import _l_
try:
    import glob
    _l_(209)

except ImportError:
    pass
try:
    import re
    _l_(211)

except ImportError:
    pass

mapfile = input("Enter map file name with extension eg. codifica.txt: ")
_l_(212)
sep = input("Enter map file column separator eg. |: ")
_l_(213)
mask = input("Enter search mask with extension eg. 2010*txt for all files to be processed: ")
_l_(214)
suff = input("Enter suffix with extension eg. _NEW.txt for newly generated files: ")
_l_(215)

rep = {} # creation of empy dictionary
_l_(216) # creation of empy dictionary

with open(mapfile) as temprep:
    _l_(220)

    for line in temprep:
        _l_(219)

        (key, val) = line.strip('\n').split(sep)
        _l_(217)
        rep[key] = val
        _l_(218)

for filename in glob.iglob(mask):
    _l_(228)


    with open (filename, "r") as textfile:
        _l_(227)

        text = textfile.read()
        _l_(221)

        # start replacement
        #rep = dict((re.escape(k), v) for k, v in rep.items()) commented to enable the use in the mapping of re reserved characters
        pattern = re.compile("|".join(rep.keys()))
        _l_(222)
        text = pattern.sub(lambda m: rep[m.group(0)], text)
        _l_(223)

        #write of te output files with the prompted suffice
        target = open(filename[:-4]+"_NEW.txt", "w")
        _l_(224)
        target.write(text)
        _l_(225)
        target.close()
        _l_(226)

