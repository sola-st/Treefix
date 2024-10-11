import numpy as np # pragma: no cover
import sys # pragma: no cover

a = b'abcdef' # pragma: no cover
b = b'ghijkl' # pragma: no cover
context = type('Mock', (object,), {'num_gpus': lambda: 0})() # pragma: no cover
ops = type('Mock', (object,), {'device': lambda x: tf.device(x).__enter__() or type('MockDevice', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_value, traceback: None})()})() # pragma: no cover
self = type('Mock', (object,), {'_run': lambda self, func, n: [func() for _ in range(n)]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

from l3.Runtime import _l_
def func():
    _l_(16166)

    aux = memoryview(a + b)
    _l_(16165)
    exit(aux)

with ops.device("GPU:0" if context.num_gpus() else "CPU:0"):
    _l_(16170)

    for _ in range(1000):
        _l_(16168)

        func()  # Warmup.
        _l_(16167)  # Warmup.
    self._run(func, 30000)
    _l_(16169)
