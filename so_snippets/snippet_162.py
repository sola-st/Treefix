# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
# Search for entry.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
for x in _n_(821919, "y", lambda: y):
  if _n_(821920, "x", lambda: x) == 3:
    found = _n_(821921, "x", lambda: x)

# Work with found entry.
try:
  _c_(821926, _n_(821922, "print", lambda: print), _c_(821925, _a_(821923, 'Found: {0}', "format"), _n_(821924, "found", lambda: found)))
except _n_(821927, "NameError", lambda: NameError):
  _c_(821929, _n_(821928, "print", lambda: print), 'Not found')
else:
  # Handle rest of Found case here
  ...

