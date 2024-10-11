from unittest.mock import Mock # pragma: no cover

seed = [1, 2] # pragma: no cover
def get_device():# pragma: no cover
    # Simple mock to simulate a GPU device.# pragma: no cover
    return Mock(name='GPU') # pragma: no cover
self = type('Mock', (object,), {'assertAllClose': lambda self, x, y: None})() # pragma: no cover

import numpy as np # pragma: no cover
from unittest.mock import Mock # pragma: no cover

case = (None, lambda seed: tf.random.stateless_uniform(shape=[3], seed=seed), None) # pragma: no cover
class ops:# pragma: no cover
    def device(name):# pragma: no cover
        return tf.device(name) # pragma: no cover
seed = (42, 42) # pragma: no cover
def get_device():# pragma: no cover
    return Mock(name='GPU') # pragma: no cover
class MockTest:# pragma: no cover
    def assertAllClose(self, x, y):# pragma: no cover
        np.testing.assert_allclose(x, y) # pragma: no cover
self = MockTest() # pragma: no cover

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
