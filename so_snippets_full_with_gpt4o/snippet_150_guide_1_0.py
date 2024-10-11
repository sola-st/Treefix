this = 'a_value' # pragma: no cover
that = 'a_different_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script
#do stuff
from l3.Runtime import _l_
if this == that:
  _l_(14283)

  quit()
  _l_(14282)

