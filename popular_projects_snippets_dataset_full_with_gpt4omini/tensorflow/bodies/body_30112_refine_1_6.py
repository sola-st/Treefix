import numpy as np # pragma: no cover

STRIDED_SLICE_TYPES = ['numpy.ndarray', 'torch.Tensor'] # pragma: no cover
class MockSelf:  # Mock for self to hold subTest method# pragma: no cover
    def subTest(self, **kwargs):# pragma: no cover
        pass# pragma: no cover
self = MockSelf() # pragma: no cover
class StridedSliceChecker:# pragma: no cover
    REF_TENSOR = np.array([1, 2, 3, 4, 5])  # Example reference tensor# pragma: no cover
    def __init__(self, context, tensor, tensor_type):# pragma: no cover
        self.tensor = tensor# pragma: no cover
        self.tensor_type = tensor_type# pragma: no cover
        self.context = context# pragma: no cover
    def __getitem__(self, slice_):# pragma: no cover
        return self.tensor[slice_] if isinstance(self.tensor, np.ndarray) else self.tensor.type(slice_) # pragma: no cover
StridedSliceChecker.REF_TENSOR = np.array([1, 2, 3, 4, 5]) # pragma: no cover

import numpy as np # pragma: no cover

STRIDED_SLICE_TYPES = ['numpy.ndarray', 'torch.Tensor'] # pragma: no cover
class MockSelf:  # Mock for self to hold subTest method# pragma: no cover
    def subTest(self, **kwargs):# pragma: no cover
        return self# pragma: no cover
self = MockSelf() # pragma: no cover
class StridedSliceChecker:# pragma: no cover
    REF_TENSOR = np.array([1, 2, 3, 4, 5])  # Example reference tensor# pragma: no cover
    def __init__(self, context, tensor, tensor_type):# pragma: no cover
        self.tensor = tensor# pragma: no cover
        self.tensor_type = tensor_type# pragma: no cover
        self.context = context# pragma: no cover
    def __getitem__(self, slice_):# pragma: no cover
        return self.tensor[slice_] # pragma: no cover
StridedSliceChecker.REF_TENSOR = np.array([1, 2, 3, 4, 5]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
from l3.Runtime import _l_
for tensor_type in STRIDED_SLICE_TYPES:
    _l_(6259)

    with self.subTest(tensor_type=tensor_type, use_gpu=True):
        _l_(6258)

        checker = StridedSliceChecker(
            self, StridedSliceChecker.REF_TENSOR, tensor_type=tensor_type)
        _l_(6243)
        _ = checker[:, :, :]
        _l_(6244)
        # Various ways of representing identity slice
        _ = checker[:, :, :]
        _l_(6245)
        _ = checker[::, ::, ::]
        _l_(6246)
        _ = checker[::1, ::1, ::1]
        _l_(6247)
        # Not zero slice
        _ = checker[::1, ::5, ::2]
        _l_(6248)
        # Reverse in each dimension independently
        _ = checker[::-1, :, :]
        _l_(6249)
        _ = checker[:, ::-1, :]
        _l_(6250)
        _ = checker[:, :, ::-1]
        _l_(6251)
        ## negative index tests i.e. n-2 in first component
        _ = checker[-2::-1, :, ::1]
        _l_(6252)
        # negative index tests i.e. n-2 in first component, non-unit stride
        _ = checker[-2::-1, :, ::2]
        _l_(6253)

        # Check rank-0 examples
        checker2 = StridedSliceChecker(self, 5, tensor_type=tensor_type)
        _l_(6254)
        _ = checker2[None]
        _l_(6255)
        _ = checker2[...]
        _l_(6256)
        _ = checker2[tuple()]
        _l_(6257)
