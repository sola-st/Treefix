self = type('Mock', (object,), {'evaluate': lambda self, x: [element.numpy() for element in x], 'assertEqual': lambda self, a, b: a == b})() # pragma: no cover
sess = type('MockSession', (object,), {'partial_run_setup': lambda self, fetches, feeds: 'handle', 'partial_run': lambda self, handle, fetch_list: [element.numpy() for element in fetch_list]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
from l3.Runtime import _l_
a = constant_op.constant(2.0, dtypes.float32)
_l_(20483)
b = a * 2
_l_(20484)
c = b * 3
_l_(20485)
r1 = self.evaluate([b, c])
_l_(20486)
h = sess.partial_run_setup([b, c], [])
_l_(20487)
r2 = sess.partial_run(h, [b, c])
_l_(20488)
self.assertEqual(r1, r2)
_l_(20489)
