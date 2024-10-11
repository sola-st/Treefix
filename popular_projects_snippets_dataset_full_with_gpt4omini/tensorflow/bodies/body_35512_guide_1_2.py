import numpy as np # pragma: no cover
import torch # pragma: no cover
from typing import List # pragma: no cover

class MockTest:  # Mock class to provide test attributes and methods # pragma: no cover
    @staticmethod # pragma: no cover
    def is_gpu_available(): # pragma: no cover
        return False # pragma: no cover
# Simulate no GPU available # pragma: no cover
    def assertTrue(self, condition): # pragma: no cover
        assert condition, 'Assertion failed!' # pragma: no cover
# Mock assertion method # pragma: no cover
 # pragma: no cover
def get_float_types() -> List[np.dtype]:  # Mock function to return float types # pragma: no cover
    return [np.float32, np.float64] # pragma: no cover
 # pragma: no cover
class Sampler:  # Mock sampler class # pragma: no cover
    def __init__(self, n, lower, upper, dtype, use_gpu): # pragma: no cover
        self.n = n # pragma: no cover
        self.lower = lower # pragma: no cover
        self.upper = upper # pragma: no cover
        self.dtype = dtype # pragma: no cover
        self.use_gpu = use_gpu # pragma: no cover
    def __call__(self):  # Sampling method # pragma: no cover
        sample = np.random.choice([0.0, 1.0], size=self.n)  # Choose between 0.0 and 1.0 # pragma: no cover
        return sample.astype(self.dtype) # pragma: no cover
# Return sampled values as specified dtype # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover
# Instantiate the mock test # pragma: no cover
self._Sampler = Sampler  # Assign the mock sampler # pragma: no cover

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
