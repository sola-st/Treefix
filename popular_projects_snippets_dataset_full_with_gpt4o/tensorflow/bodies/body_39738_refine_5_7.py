import numpy as np # pragma: no cover

ops = type('MockOps', (object,), {'device': lambda self, x: self})() # pragma: no cover
context = type('MockContext', (object,), {'num_gpus': lambda self: 1})() # pragma: no cover
self = type('MockSelf', (object,), {'_run': lambda self, func, times: [func() for _ in range(times)]})() # pragma: no cover
a = np.array([1], dtype=np.uint8) # pragma: no cover
b = np.array([2], dtype=np.uint8) # pragma: no cover

import numpy as np # pragma: no cover

class MockContextManager:# pragma: no cover
    def __init__(self, enter_return):# pragma: no cover
        self.enter_return = enter_return# pragma: no cover
# pragma: no cover
    def __enter__(self):# pragma: no cover
        return self.enter_return# pragma: no cover
# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        pass # pragma: no cover
ops = type('MockOps', (object,), {'device': lambda self, x: MockContextManager(enter_return=None)})() # pragma: no cover
context = type('MockContext', (object,), {'num_gpus': lambda self: 1})() # pragma: no cover
self = type('MockSelf', (object,), {'_run': lambda self, func, times: [func() for _ in range(times)]})() # pragma: no cover
a = np.array([1], dtype=np.uint8) # pragma: no cover
b = np.array([2], dtype=np.uint8) # pragma: no cover

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
