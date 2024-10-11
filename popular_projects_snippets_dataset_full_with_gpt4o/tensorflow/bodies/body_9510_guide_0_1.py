mock_self_evaluate = lambda values: values # pragma: no cover
mock_self = type('Mock', (object,), {'evaluate': mock_self_evaluate})() # pragma: no cover
mock_sess_partial_run_setup = lambda fetches, feeds: 'handle' # pragma: no cover
mock_sess_partial_run = lambda handle, fetches: [value.numpy() for value in fetches] # pragma: no cover
mock_sess = type('Mock', (object,), {'partial_run_setup': mock_sess_partial_run_setup, 'partial_run': mock_sess_partial_run})() # pragma: no cover
self = mock_self # pragma: no cover
sess = mock_sess # pragma: no cover

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
