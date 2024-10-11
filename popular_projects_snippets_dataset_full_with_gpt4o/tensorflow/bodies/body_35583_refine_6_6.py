import numpy as np # pragma: no cover

case = (None, lambda seed: np.random.RandomState(seed=seed).rand(), None) # pragma: no cover
class ops:# pragma: no cover
    @staticmethod# pragma: no cover
    def device(name):# pragma: no cover
        return tf.device(name) # pragma: no cover
seed = 42 # pragma: no cover
def get_device():# pragma: no cover
    class Device:# pragma: no cover
        @staticmethod# pragma: no cover
        def name():# pragma: no cover
            return 'GPU:0'# pragma: no cover
    return Device() # pragma: no cover
class MockTest:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertAllClose(a, b):# pragma: no cover
        np.testing.assert_allclose(a, b) # pragma: no cover
self = MockTest # pragma: no cover

import numpy as np # pragma: no cover

case = (None, lambda seed: tf.random.stateless_uniform(shape=[3], seed=(seed, seed)), None) # pragma: no cover
class ops:# pragma: no cover
    @staticmethod# pragma: no cover
    def device(name):# pragma: no cover
        return tf.device(name) # pragma: no cover
seed = 42 # pragma: no cover
def get_device():# pragma: no cover
    class Device:# pragma: no cover
        @staticmethod# pragma: no cover
        def name():# pragma: no cover
            return 'GPU:0'# pragma: no cover
    return Device() # pragma: no cover
class MockTest:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertAllClose(a, b):# pragma: no cover
        np.testing.assert_allclose(a, b) # pragma: no cover
self = MockTest # pragma: no cover

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
