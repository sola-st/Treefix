import numpy as np # pragma: no cover
import contextlib # pragma: no cover
import sys # pragma: no cover

a = np.random.rand(10).astype(np.float32).tobytes() # pragma: no cover
b = np.random.rand(10).astype(np.float32).tobytes() # pragma: no cover
context = type('MockContext', (object,), {'num_gpus': lambda: 1})() # pragma: no cover
ops = type('MockOps', (object,), {'device': contextlib.nullcontext})() # pragma: no cover
self = type('MockSelf', (object,), {'_run': lambda self, func, times: [func() for _ in range(times)]})() # pragma: no cover

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
