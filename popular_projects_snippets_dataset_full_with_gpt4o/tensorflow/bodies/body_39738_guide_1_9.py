import numpy as np # pragma: no cover
import sys # pragma: no cover
from types import SimpleNamespace # pragma: no cover

a = np.array([1, 2, 3], dtype=np.uint8).tobytes() # pragma: no cover
b = np.array([4, 5, 6], dtype=np.uint8).tobytes() # pragma: no cover
context = SimpleNamespace(num_gpus=lambda: 0) # pragma: no cover
ops = SimpleNamespace(device=lambda x: SimpleNamespace(__enter__=lambda: None, __exit__=lambda *args: None)) # pragma: no cover
self = SimpleNamespace(_run=lambda func, times: [func() for _ in range(times)]) # pragma: no cover
exit = sys.exit # pragma: no cover

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
