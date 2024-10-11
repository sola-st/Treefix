import numpy as np # pragma: no cover

STRIDED_SLICE_TYPES = ['numpy', 'tensorflow'] # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
setattr(self, 'subTest', lambda **kwargs: None) # pragma: no cover
class StridedSliceChecker: # pragma: no cover
    REF_TENSOR = np.array([[1, 2], [3, 4]]) # pragma: no cover
    def __init__(self, context, tensor, tensor_type): # pragma: no cover
        self.context = context # pragma: no cover
        self.tensor = tensor # pragma: no cover
        self.tensor_type = tensor_type # pragma: no cover
    def __getitem__(self, item): # pragma: no cover
        # Simulate tensor slicing -- in practice this should return a new slice of the tensor # pragma: no cover
        return self.tensor[item] # pragma: no cover

import numpy as np # pragma: no cover

STRIDED_SLICE_TYPES = ['float32', 'float64', 'int32', 'int64'] # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
class SubTestContextManager: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        pass # pragma: no cover
self.subTest = lambda **kwargs: SubTestContextManager() # pragma: no cover
class StridedSliceChecker: # pragma: no cover
    REF_TENSOR = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # pragma: no cover
    def __init__(self, context, tensor, tensor_type): # pragma: no cover
        self.context = context # pragma: no cover
        self.tensor = tensor # pragma: no cover
        self.tensor_type = tensor_type # pragma: no cover
    def __getitem__(self, item): # pragma: no cover
        return self.tensor[item] # pragma: no cover

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
