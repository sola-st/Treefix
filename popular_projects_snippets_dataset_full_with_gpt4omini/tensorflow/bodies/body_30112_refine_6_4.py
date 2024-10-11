from typing import Any, Tuple # pragma: no cover

STRIDED_SLICE_TYPES = ['float32', 'float64', 'int32', 'int64'] # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.subTest = lambda **kwargs: None # pragma: no cover
class StridedSliceChecker: # pragma: no cover
    REF_TENSOR = 'reference_tensor' # pragma: no cover
    def __init__(self, context: Any, tensor: Any, tensor_type: str): # pragma: no cover
        self.context = context # pragma: no cover
        self.tensor = tensor # pragma: no cover
        self.tensor_type = tensor_type # pragma: no cover
    def __getitem__(self, item: Any) -> Any: # pragma: no cover
        return f'slice: {item}' # pragma: no cover
StridedSliceChecker = StridedSliceChecker # pragma: no cover

import numpy as np # pragma: no cover

STRIDED_SLICE_TYPES = ['float32', 'float64', 'int32', 'int64'] # pragma: no cover
class MockSelf: # pragma: no cover
    def subTest(self, **kwargs): # pragma: no cover
        return self # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        pass# pragma: no cover
self = MockSelf() # pragma: no cover
class StridedSliceChecker: # pragma: no cover
    REF_TENSOR = np.array([[1, 2], [3, 4], [5, 6]]) # pragma: no cover
    def __init__(self, context, tensor, tensor_type): # pragma: no cover
        self.context = context # pragma: no cover
        self.tensor = tensor # pragma: no cover
        self.tensor_type = tensor_type # pragma: no cover
    def __getitem__(self, slice_obj): # pragma: no cover
        return self.tensor[slice_obj]# pragma: no cover
 # pragma: no cover
checker = StridedSliceChecker(self, StridedSliceChecker.REF_TENSOR, STRIDED_SLICE_TYPES[0]) # pragma: no cover

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
