# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-variable-is-a-function
from l3.Runtime import _l_
def myfunc(x):
  _l_(1676)

  try:
    _l_(1675)

    x()
    _l_(1672)
  except TypeError:
    _l_(1674)

    raise Exception("Not callable")
    _l_(1673)

