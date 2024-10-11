import numpy as np # pragma: no cover

ops = type('Mock', (object,), {'device': lambda device: tf.device(device)})() # pragma: no cover
context = type('Mock', (object,), {'num_gpus': lambda: tf.config.list_physical_devices('GPU')})() # pragma: no cover
self = type('Mock', (object,), {'_run': lambda func, num: [func() for _ in range(num)]})() # pragma: no cover
a = np.array([1, 2, 3, 4]) # pragma: no cover
b = np.array([5, 6, 7, 8]) # pragma: no cover

import numpy as np # pragma: no cover

class MockDeviceContextManager:# pragma: no cover
    def __init__(self, device):# pragma: no cover
        self.device = device# pragma: no cover
    def __enter__(self):# pragma: no cover
        tf.device(self.device).__enter__()# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        tf.device(self.device).__exit__(exc_type, exc_value, traceback) # pragma: no cover
ops = type('MockOps', (object,), {'device': MockDeviceContextManager}) # pragma: no cover
context = type('MockContext', (object,), {'num_gpus': lambda: len(tf.config.list_physical_devices('GPU'))})() # pragma: no cover
self = type('MockSelf', (object,), {'_run': lambda self, func, num: [func() for _ in range(num)]})() # pragma: no cover
a = np.array([1, 2, 3, 4]) # pragma: no cover
b = np.array([5, 6, 7, 8]) # pragma: no cover

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
