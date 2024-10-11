import numpy as np # pragma: no cover
import torch # pragma: no cover

class MockTest:  # Mock for the test object # pragma: no cover
    @staticmethod # pragma: no cover
    def is_gpu_available(): # pragma: no cover
        return False # pragma: no cover
    def assertTrue(self, condition): # pragma: no cover
        assert condition, 'Assertion failed' # pragma: no cover
 # pragma: no cover
class MockSampler:  # Mock for the sampler # pragma: no cover
    def __init__(self, num_samples, lower, upper, dtype, use_gpu): # pragma: no cover
        self.num_samples = num_samples # pragma: no cover
        self.lower = lower # pragma: no cover
        self.upper = upper # pragma: no cover
        self.dtype = dtype # pragma: no cover
        self.use_gpu = use_gpu # pragma: no cover
    def __call__(self): # pragma: no cover
        return np.random.uniform(self.lower, self.upper, self.num_samples).astype(self.dtype) # pragma: no cover
 # pragma: no cover
def get_float_types(): # pragma: no cover
    return [np.float32, np.float64] # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover
self._Sampler = MockSampler # pragma: no cover

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
