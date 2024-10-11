import numpy as np # pragma: no cover
import sys # pragma: no cover

context = type("MockContext", (object,), {"num_gpus": lambda: 1})() # pragma: no cover
self = type("MockSelf", (object,), {"_run": lambda self, func, num: [func() for _ in range(num)]})() # pragma: no cover
a = np.array([1, 2, 3], dtype=np.int8) # pragma: no cover
b = np.array([4, 5, 6], dtype=np.int8) # pragma: no cover

import numpy as np # pragma: no cover
import sys # pragma: no cover

class MockOps: # pragma: no cover
    def device(self, device_name): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                pass # pragma: no cover
        return ContextManager() # pragma: no cover
ops = MockOps() # pragma: no cover
 # pragma: no cover
class MockContext: # pragma: no cover
    def num_gpus(self): # pragma: no cover
        return 1 # pragma: no cover
context = MockContext() # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def _run(self, func, num): # pragma: no cover
        for _ in range(num): # pragma: no cover
            func() # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
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
