import numpy as np # pragma: no cover
import contextlib # pragma: no cover

a = np.array([1, 2, 3]) # pragma: no cover
b = np.array([4, 5, 6]) # pragma: no cover
context = type('Mock', (), {'num_gpus': lambda: 1})() # pragma: no cover
ops = type('Mock', (), {'device': contextlib.contextmanager(lambda x: (yield))})() # pragma: no cover
self = type('Mock', (), {'_run': lambda f, n: [f() for _ in range(n)]})() # pragma: no cover

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
