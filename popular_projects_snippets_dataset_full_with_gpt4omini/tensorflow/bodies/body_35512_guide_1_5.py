import numpy as np # pragma: no cover
import torch # pragma: no cover

class MockTest:  # Mock class to simulate testing behavior # pragma: no cover
    @staticmethod # pragma: no cover
    def is_gpu_available(): # pragma: no cover
        return False # pragma: no cover
# Simulating the absence of a GPU # pragma: no cover
    def assertTrue(self, condition): # pragma: no cover
        assert condition, 'Assertion failed!' # pragma: no cover
# Mock assertion method # pragma: no cover
 # pragma: no cover
def get_float_types():  # Function to provide float types # pragma: no cover
    return [np.float32, np.float64] # pragma: no cover
 # pragma: no cover
class MockSampler:  # Mock for the sampler class # pragma: no cover
    def __init__(self, size, low, high, dtype, use_gpu): # pragma: no cover
        self.size = size # pragma: no cover
        self.low = low # pragma: no cover
        self.high = high # pragma: no cover
        self.dtype = dtype # pragma: no cover
        self.use_gpu = use_gpu # pragma: no cover
    def __call__(self): # pragma: no cover
        # Return samples; repeat a few values to ensure count >= 10 # pragma: no cover
        return np.array([0.5] * 15 + [0.6] * (self.size - 15), dtype=self.dtype) # pragma: no cover
# Example array # pragma: no cover
 # pragma: no cover
test = MockTest() # pragma: no cover
self = type('Test', (), {'_Sampler': MockSampler, 'assertTrue': test.assertTrue})() # pragma: no cover

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
