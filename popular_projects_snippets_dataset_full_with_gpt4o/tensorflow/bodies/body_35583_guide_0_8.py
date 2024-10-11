seed = [1, 2] # pragma: no cover
class MockDevice:# pragma: no cover
    def name(self):# pragma: no cover
        return 'GPU:0' # pragma: no cover
get_device = MockDevice() # pragma: no cover
class MockSelf:# pragma: no cover
    def assertAllClose(self, a, b):# pragma: no cover
        assert tf.reduce_all(tf.math.equal(a, b)), f"Values {a} and {b} are not close" # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
# Stateless ops should produce the same result on CPUs and GPUs.
from l3.Runtime import _l_
_, stateless_op, _ = case
_l_(20577)

with ops.device('CPU'):
    _l_(20579)

    result_cpu = stateless_op(seed=seed)
    _l_(20578)

with ops.device(get_device().name):
    _l_(20582)

    result_gpu = stateless_op(seed=seed)
    _l_(20580)
    self.assertAllClose(result_cpu, result_gpu)
    _l_(20581)
