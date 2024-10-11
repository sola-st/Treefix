class MockSelf:  # Mock object for 'self'# pragma: no cover
    def evaluate(self, values):# pragma: no cover
        return [val.numpy() for val in values]# pragma: no cover
    def assertEqual(self, a, b):# pragma: no cover
        assert a == b, f'Assertion failed: {a} != {b}'# pragma: no cover
self = MockSelf() # pragma: no cover
class MockSession:  # Mock object for TensorFlow session# pragma: no cover
    def partial_run_setup(self, fetches, feed_dict):# pragma: no cover
        return 'mock_session'# pragma: no cover
    def partial_run(self, handle, fetches):# pragma: no cover
        return [tf.constant(4.0), tf.constant(12.0)]  # simulate output for b and c# pragma: no cover
sess = MockSession() # pragma: no cover

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
