n = 10 # pragma: no cover
ag = type('Mock', (object,), {'set_element_type': lambda l, t: None, 'stack': lambda l, strict: l})() # pragma: no cover

n = 10 # pragma: no cover
ag = type('Mock', (object,), {'set_element_type': lambda l, t: None, 'stack': lambda l, strict: l})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_list_test.py
from l3.Runtime import _l_
l = []
_l_(20354)
l.append(1)
_l_(20355)
l.append(1)
_l_(20356)
ag.set_element_type(l, tf.int32)
_l_(20357)
for i in range(2, n):
    _l_(20360)

    l.append(l[i-1] + l[i-2])
    _l_(20358)
    l[i-2] = -l[i-2]
    _l_(20359)
aux = ag.stack(l, strict=False)
_l_(20361)
exit(aux)
