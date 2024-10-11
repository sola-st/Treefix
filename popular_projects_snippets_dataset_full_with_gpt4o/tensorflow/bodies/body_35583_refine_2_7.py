import numpy as np # pragma: no cover
import unittest # pragma: no cover

case = (None, lambda seed: np.random.RandomState(seed).rand(), None) # pragma: no cover
seed = 42 # pragma: no cover
get_device = lambda: tf.config.experimental.list_physical_devices('GPU')[0] # pragma: no cover
self = type('Mock', (unittest.TestCase,), {'assertAllClose': lambda self, x, y: np.testing.assert_allclose(x, y)})() # pragma: no cover

case = (None, lambda seed: tf.random.stateless_uniform(shape=[3], seed=(seed, seed)), None) # pragma: no cover
seed = 42 # pragma: no cover
get_device = lambda: type('Mock', (object,), {'name': 'GPU:0'})() # pragma: no cover
self = type('Mock', (object,), {'assertAllClose': lambda self, x, y: tf.debugging.assert_near(x, y)})() # pragma: no cover

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
