import numpy as np # pragma: no cover

import numpy as np # pragma: no cover

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
