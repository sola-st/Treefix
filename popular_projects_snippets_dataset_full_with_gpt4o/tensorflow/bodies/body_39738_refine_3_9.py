import numpy as np # pragma: no cover
from types import SimpleNamespace # pragma: no cover

ops = type('Mock', (object,), {'device': lambda x: context})() # pragma: no cover
context = type('Mock', (object,), {'num_gpus': lambda: 1})() # pragma: no cover
self = type('Mock', (object,), {'_run': lambda func, n: [func() for _ in range(n)]})() # pragma: no cover
a = np.array([1, 2, 3]) # pragma: no cover
b = np.array([4, 5, 6]) # pragma: no cover

import numpy as np # pragma: no cover

class MockContextManager: # pragma: no cover
    def __init__(self, device): # pragma: no cover
        self.device = device # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self.device # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
ops = type('MockOps', (object,), {'device': lambda self, device: MockContextManager(device)})() # pragma: no cover
context = type('MockContext', (object,), {'num_gpus': lambda self: len(tf.config.list_physical_devices('GPU'))})() # pragma: no cover
self = type('MockSelf', (object,), {'_run': lambda self, func, runs: [func() for _ in range(runs)]})() # pragma: no cover
a = np.array([1, 2, 3], dtype=np.int8) # pragma: no cover
b = np.array([4, 5, 6], dtype=np.int8) # pragma: no cover

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
