from collections import defaultdict # pragma: no cover

someddict = collections.defaultdict(int) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
from l3.Runtime import _l_
somedict = {}
_l_(12707)
print(somedict[3]) # KeyError
_l_(12708) # KeyError

someddict = defaultdict(int)
_l_(12709)
print(someddict[3]) # print int(), thus 0
_l_(12710) # print int(), thus 0

