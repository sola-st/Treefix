import random # pragma: no cover

case = ('test', lambda seed: random.Random(seed).randint(1, 100), 'additional') # pragma: no cover
seed = 42 # pragma: no cover
get_device = type('MockDevice', (object,), {'name': 'GPU'})() # pragma: no cover

seed = (42, 24) # pragma: no cover
get_device = lambda: type('Mock', (object,), {'name': 'GPU:0'})() # pragma: no cover
self = type('Mock', (object,), {'assertAllClose': lambda self, x, y: tf.debugging.assert_near(x, y, atol=1e-6)})() # pragma: no cover

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
