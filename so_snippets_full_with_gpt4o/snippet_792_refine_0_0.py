class Pump:# pragma: no cover
    def getPumps(self):# pragma: no cover
        pass # pragma: no cover

class Pump:# pragma: no cover
    @staticmethod# pragma: no cover
    def getPumps():# pragma: no cover
        pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
# WRONG! will result in TypeError: getPumps() missing 1 required positional argument: 'self'
from l3.Runtime import _l_
p = Pump
_l_(14692)
p.getPumps()
_l_(14693)

# CORRECT!
p = Pump()
_l_(14694)
p.getPumps()
_l_(14695)

