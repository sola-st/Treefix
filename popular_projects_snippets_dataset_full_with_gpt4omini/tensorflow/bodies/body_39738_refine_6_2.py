import numpy as np # pragma: no cover

context = type('MockContext', (object,), {'num_gpus': lambda: 1})() # pragma: no cover
self = type('MockSelf', (object,), {'_run': lambda f, t: f()})() # pragma: no cover
a = np.random.rand(10, 10).astype(np.float32) # pragma: no cover
b = np.random.rand(10, 10).astype(np.float32) # pragma: no cover

import numpy as np # pragma: no cover

class MockOps:  # Mocking the ops object# pragma: no cover
    def device(self, device_str): return device_str# pragma: no cover
ops = MockOps() # pragma: no cover
class MockContext:  # Mocking the context object# pragma: no cover
    def num_gpus(self): return 1# pragma: no cover
context = MockContext() # pragma: no cover
class MockSelf:  # Mocking the self object# pragma: no cover
    def _run(self, func, duration): func()# pragma: no cover
self = MockSelf() # pragma: no cover
a = np.random.rand(1000).astype(np.float32) # pragma: no cover
b = np.random.rand(1000).astype(np.float32) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

from l3.Runtime import _l_
def func():
    _l_(4421)

    aux = memoryview(a + b)
    _l_(4420)
    exit(aux)

with ops.device("GPU:0" if context.num_gpus() else "CPU:0"):
    _l_(4425)

    for _ in range(1000):
        _l_(4423)

        func()  # Warmup.
        _l_(4422)  # Warmup.
    self._run(func, 30000)
    _l_(4424)
