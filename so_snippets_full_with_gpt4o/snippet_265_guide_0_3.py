# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-variable-is-a-function
from l3.Runtime import _l_
def myfunc(x):
  _l_(13928)

  try:
    _l_(13927)

    x()
    _l_(13924)
  except TypeError:
    _l_(13926)

    raise Exception("Not callable")
    _l_(13925)

