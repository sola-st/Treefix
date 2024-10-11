# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
from l3.Runtime import _l_
try:
     import re
     _l_(3395)

except ImportError:
     pass

name = ["A1B1", "djdd", "B2C4", "C2H2", "jdoi","1A4V"]
_l_(3396)

# Match names.
for element in name:
     _l_(3400)

     m = re.match("(^[A-Z]\d[A-Z]\d)", element)
     _l_(3397)
     if m:
          _l_(3399)

          print(m.groups())
          _l_(3398)

