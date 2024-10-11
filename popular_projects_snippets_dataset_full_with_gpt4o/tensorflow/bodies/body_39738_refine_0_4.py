import numpy as np # pragma: no cover
import sys # pragma: no cover

context = type("MockContext", (object,), {"num_gpus": lambda: 1})() # pragma: no cover
self = type("MockSelf", (object,), {"_run": lambda self, func, num: [func() for _ in range(num)]})() # pragma: no cover
a = np.array([1, 2, 3], dtype=np.int8) # pragma: no cover
b = np.array([4, 5, 6], dtype=np.int8) # pragma: no cover

import numpy as np # pragma: no cover
import sys # pragma: no cover

class MockOps:  # pragma: no cover
    def device(self, device_name): # pragma: no cover
        return self # pragma: no cover
    def __enter__(self): # pragma: no cover
        pass # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        pass # pragma: no cover
ops = MockOps() # pragma: no cover
context = type("MockContext", (object,), {"num_gpus": lambda: 1})() # pragma: no cover
self = type("MockSelf", (object,), {"_run": lambda self, func, num: [func() for _ in range(num)]})() # pragma: no cover
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
