import mock # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string
from l3.Runtime import _l_
try:
   import inspect
   _l_(2535)

except ImportError:
   pass

def foo():
   _l_(2537)

   print(inspect.stack()[0][3])
   _l_(2536)

