self = type('Mock', (object,), {'evaluate': lambda self, x: [4.0, 12.0], 'assertEqual': lambda self, a, b: print('Assert Equal:', a == b)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
from l3.Runtime import _l_
a = constant_op.constant(2.0, dtypes.float32)
_l_(7431)
b = a * 2
_l_(7432)
c = b * 3
_l_(7433)
r1 = self.evaluate([b, c])
_l_(7434)
h = sess.partial_run_setup([b, c], [])
_l_(7435)
r2 = sess.partial_run(h, [b, c])
_l_(7436)
self.assertEqual(r1, r2)
_l_(7437)
