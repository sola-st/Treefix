from collections import defaultdict # pragma: no cover

defaultdict = defaultdict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
from l3.Runtime import _l_
somedict = {}
_l_(518)
print(somedict[3]) # KeyError
_l_(519) # KeyError

someddict = defaultdict(int)
_l_(520)
print(someddict[3]) # print int(), thus 0
_l_(521) # print int(), thus 0

