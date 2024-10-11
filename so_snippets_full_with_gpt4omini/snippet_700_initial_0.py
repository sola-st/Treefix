condition = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
from l3.Runtime import _l_
if condition:
       _l_(2000)

       try:
              import recommend
              _l_(1999)

       except ImportError:
              pass

