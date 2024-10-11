import numpy as np # pragma: no cover
import sys # pragma: no cover
from contextlib import contextmanager # pragma: no cover

a = np.array([1, 2, 3], dtype=np.uint8).tobytes() # pragma: no cover
b = np.array([4, 5, 6], dtype=np.uint8).tobytes() # pragma: no cover
context = type('Mock', (object,), {'num_gpus': lambda: 0})() # pragma: no cover
ops = type('Mock', (object,), {'device': lambda x: contextmanager(lambda: iter([None]))()})() # pragma: no cover
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
