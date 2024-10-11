import numpy as np # pragma: no cover
import contextlib # pragma: no cover

a = np.array([1, 2, 3], dtype=np.int32) # pragma: no cover
b = np.array([4, 5, 6], dtype=np.int32) # pragma: no cover
class MockContext:# pragma: no cover
    def num_gpus(self): return 1# pragma: no cover
context = MockContext() # pragma: no cover
class MockOps:# pragma: no cover
    @contextlib.contextmanager# pragma: no cover
    def device(self, device_name):# pragma: no cover
        yield# pragma: no cover
ops = MockOps() # pragma: no cover
class MockSelf:# pragma: no cover
    def _run(self, func, times):# pragma: no cover
        for _ in range(times):# pragma: no cover
            func()  # pragma: no cover
self = MockSelf() # pragma: no cover

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
