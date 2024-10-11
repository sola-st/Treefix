import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
ag = Mock() # pragma: no cover
ag.set_element_type = lambda lst, dtype: None # pragma: no cover
ag.stack = lambda lst, strict: lst # pragma: no cover
n = 10 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_list_test.py
from l3.Runtime import _l_
l = []
_l_(7339)
l.append(1)
_l_(7340)
l.append(1)
_l_(7341)
ag.set_element_type(l, tf.int32)
_l_(7342)
for i in range(2, n):
    _l_(7345)

    l.append(l[i-1] + l[i-2])
    _l_(7343)
    l[i-2] = -l[i-2]
    _l_(7344)
aux = ag.stack(l, strict=False)
_l_(7346)
exit(aux)
