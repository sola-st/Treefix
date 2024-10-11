import numpy as np # pragma: no cover

case = (None, lambda seed: np.random.RandomState(seed).rand(2, 2), None) # pragma: no cover
seed = 42 # pragma: no cover
get_device = lambda: tf.device('/GPU:0' if tf.config.list_physical_devices('GPU') else '/CPU:0') # pragma: no cover
self = type('Mock', (object,), {'assertAllClose': lambda self, x, y: np.allclose(x, y)})() # pragma: no cover

import numpy as np # pragma: no cover

seed = (42, 43) # pragma: no cover
get_device = lambda: tf.device('/GPU:0') if tf.config.experimental.list_physical_devices('GPU') else tf.device('/CPU:0') # pragma: no cover
class MockSelf: # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        assert np.allclose(a, b) # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
# Stateless ops should produce the same result on CPUs and GPUs.
from l3.Runtime import _l_
_, stateless_op, _ = case
_l_(7475)

with ops.device('CPU'):
    _l_(7477)

    result_cpu = stateless_op(seed=seed)
    _l_(7476)

with ops.device(get_device().name):
    _l_(7480)

    result_gpu = stateless_op(seed=seed)
    _l_(7478)
    self.assertAllClose(result_cpu, result_gpu)
    _l_(7479)
