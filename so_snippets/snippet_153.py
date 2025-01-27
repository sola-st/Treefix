# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
for i in (1, 10, 100):
    _c_(821964, _n_(821960, "print", lambda: print), _c_(821963, _a_(821961, '{num:02d}', "format"), num=_n_(821962, "i", lambda: i)))

_c_(821969, _n_(821965, "print", lambda: print), _c_(821968, _n_(821966, "format", lambda: format), _n_(821967, "i", lambda: i), '02d'))

