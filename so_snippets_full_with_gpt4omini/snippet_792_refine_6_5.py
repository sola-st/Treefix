class Pump:# pragma: no cover
    def getPumps(self):# pragma: no cover
        return 'List of pumps' # pragma: no cover
Pump = Pump # pragma: no cover

class Pump:# pragma: no cover
    def getPumps(self):# pragma: no cover
        return 'Pumps retrieved' # pragma: no cover

p = Pump() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
# WRONG! will result in TypeError: getPumps() missing 1 required positional argument: 'self'
from l3.Runtime import _l_
p = Pump
_l_(2325)
p.getPumps()
_l_(2326)

# CORRECT!
p = Pump()
_l_(2327)
p.getPumps()
_l_(2328)

