class Mock:# pragma: no cover
    def get_result_as_array(self):# pragma: no cover
        return [1, 2, 3]# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
from l3.Runtime import _l_
aux = list(self.get_result_as_array())
_l_(10304)
exit(aux)
