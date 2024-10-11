class MockSelf:  # Mocking self object# pragma: no cover
    def evaluate(self, tensors):# pragma: no cover
        return [t.numpy() for t in tensors]# pragma: no cover
    def assertEqual(self, first, second):# pragma: no cover
        assert first == second, f'Assertion failed: {first} != {second}'# pragma: no cover
self = MockSelf() # pragma: no cover
class MockSession:  # Mocking TensorFlow session# pragma: no cover
    def partial_run_setup(self, tensors, feed_dict):# pragma: no cover
        return 'mock_setup'  # Return a mock identifier# pragma: no cover
    def partial_run(self, handle, tensors):# pragma: no cover
        return [t * 2 * 3 for t in tensors]  # Simulate computation# pragma: no cover
sess = MockSession() # pragma: no cover

class MockSelf:# pragma: no cover
    def evaluate(self, tensors):# pragma: no cover
        return [t.numpy() for t in tensors]# pragma: no cover
    def assertEqual(self, first, second):# pragma: no cover
        assert first == second, f'Assertion failed: {first} != {second}'# pragma: no cover
self = MockSelf() # pragma: no cover
class MockSession:# pragma: no cover
    def partial_run_setup(self, tensors, feed_dict):# pragma: no cover
        return 'mock_setup'# pragma: no cover
    def partial_run(self, handle, tensors):# pragma: no cover
        return [t * 2 * 3 for t in tensors]# pragma: no cover
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
