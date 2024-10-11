 # pragma: no cover
class MockSession: # pragma: no cover
    def partial_run_setup(self, fetches, feeds): # pragma: no cover
        return 'mock_handle' # pragma: no cover
 # pragma: no cover
    def partial_run(self, handle, fetches): # pragma: no cover
        return tf.compat.v1.get_default_session().run(fetches) # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def evaluate(self, tensors): # pragma: no cover
        sess = tf.compat.v1.get_default_session() # pragma: no cover
        return sess.run(tensors) # pragma: no cover
 # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b # pragma: no cover
 # pragma: no cover
sess = MockSession() # pragma: no cover
self = MockSelf() # pragma: no cover

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
