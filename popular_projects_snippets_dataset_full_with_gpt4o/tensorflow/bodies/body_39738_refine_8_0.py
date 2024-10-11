import numpy as np # pragma: no cover

ops = type('Mock', (object,), {'device': lambda x: context}) # pragma: no cover
context = type('Mock', (object,), {'num_gpus': lambda: 1}) # pragma: no cover
self = type('Mock', (object,), {'_run': lambda x, y: None}) # pragma: no cover
a = np.array([1, 2, 3]) # pragma: no cover
b = np.array([4, 5, 6]) # pragma: no cover

import numpy as np # pragma: no cover

ops = type('Mock', (object,), {'device': lambda self, x: type('DeviceContext', (object,), {'__enter__': lambda s: None, '__exit__': lambda s, exc_type, exc_value, traceback: None})()})() # pragma: no cover
context = type('Mock', (object,), {'num_gpus': lambda self: 1})() # pragma: no cover
self = type('Mock', (object,), {'_run': lambda self, func, times: [func() for _ in range(times)]})() # pragma: no cover
a = np.array([1, 2, 3], dtype=np.uint8) # pragma: no cover
b = np.array([4, 5, 6], dtype=np.uint8) # pragma: no cover

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
