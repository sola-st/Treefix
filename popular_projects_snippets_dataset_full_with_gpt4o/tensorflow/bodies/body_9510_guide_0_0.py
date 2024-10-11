class MockSess: # pragma: no cover
    def partial_run_setup(self, fetches, feeds): # pragma: no cover
        return 'mock_handle' # pragma: no cover
    def partial_run(self, handle, fetches): # pragma: no cover
        return [fetch.eval(session=tf.compat.v1.Session()) for fetch in fetches] # pragma: no cover
sess = MockSess() # pragma: no cover
class MockTest: # pragma: no cover
    def evaluate(self, tensors): # pragma: no cover
        return [tensor.eval(session=tf.compat.v1.Session()) for tensor in tensors] # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b # pragma: no cover
self = MockTest() # pragma: no cover

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
