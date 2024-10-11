seed = [1, 2] # pragma: no cover
case = (None, lambda seed: tf.random.stateless_uniform(shape=[10], seed=seed), None) # pragma: no cover
class MockDevice: # pragma: no cover
    def name(self): # pragma: no cover
        return '/device:GPU:0' # pragma: no cover
def get_device(): # pragma: no cover
    return MockDevice() # pragma: no cover
class MockTestCase: # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        tf.debugging.assert_near(a, b) # pragma: no cover
self = MockTestCase() # pragma: no cover

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
