import numpy as np # pragma: no cover
from scipy.stats import truncnorm # pragma: no cover
import torch # pragma: no cover
import unittest # pragma: no cover

class MockTest:  # Mock class to provide attributes and methods # pragma: no cover
    @staticmethod # pragma: no cover
    def is_gpu_available(): # pragma: no cover
        return False # pragma: no cover
# Simulate that GPU is not available # pragma: no cover
    def _Sampler(self, size, a, b, dtype, use_gpu): # pragma: no cover
        class Sampler: # pragma: no cover
# Define a mock sampler class # pragma: no cover
            def __init__(self, size, a, b, dtype, use_gpu): # pragma: no cover
                self.size = size # pragma: no cover
                self.a = a # pragma: no cover
                self.b = b # pragma: no cover
                self.dtype = dtype # pragma: no cover
                self.use_gpu = use_gpu # pragma: no cover
            def __call__(self): # pragma: no cover
                return np.random.normal(loc=(self.a + self.b) / 2, scale=(self.b - self.a) / 4, size=self.size).astype(self.dtype) # pragma: no cover
# Sampling method # pragma: no cover
        return Sampler(size, a, b, dtype, use_gpu) # pragma: no cover
# Return a sampler instance # pragma: no cover
def get_float_types(): # pragma: no cover
    return [np.float32, np.float64] # pragma: no cover
# Provide float types # pragma: no cover
self = MockTest() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
# NOTE: TruncatedNormal on GPU is not supported.
from l3.Runtime import _l_
if not test.is_gpu_available():
    _l_(8670)

    for dt in get_float_types():
        _l_(8669)

        sampler = self._Sampler(1000, 0.0, 1.0, dt, use_gpu=False)
        _l_(8660)
        x = sampler()
        _l_(8661)
        y = sampler()
        _l_(8662)
        # Number of different samples.
        count = (x == y).sum()
        _l_(8663)
        if count >= 10:
            _l_(8667)

            print("x = ", x)
            _l_(8664)
            print("y = ", y)
            _l_(8665)
            print("count = ", count)
            _l_(8666)
        self.assertTrue(count < 10)
        _l_(8668)
