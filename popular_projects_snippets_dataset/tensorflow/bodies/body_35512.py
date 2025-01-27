# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
# NOTE: TruncatedNormal on GPU is not supported.
from l3.Runtime import _l_
if not test.is_gpu_available():
    _l_(21448)

    for dt in get_float_types():
        _l_(21447)

        sampler = self._Sampler(1000, 0.0, 1.0, dt, use_gpu=False)
        _l_(21438)
        x = sampler()
        _l_(21439)
        y = sampler()
        _l_(21440)
        # Number of different samples.
        count = (x == y).sum()
        _l_(21441)
        if count >= 10:
            _l_(21445)

            print("x = ", x)
            _l_(21442)
            print("y = ", y)
            _l_(21443)
            print("count = ", count)
            _l_(21444)
        self.assertTrue(count < 10)
        _l_(21446)
