import numpy as np # pragma: no cover
from typing import List, Any # pragma: no cover
import unittest # pragma: no cover

STRIDED_SLICE_TYPES = [np.ndarray, list] # pragma: no cover
class StridedSliceChecker: # pragma: no cover
    REF_TENSOR = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # pragma: no cover
    def __init__(self, test_case, reference_tensor, tensor_type): # pragma: no cover
        self.test_case = test_case # pragma: no cover
        self.tensor = tensor_type(reference_tensor) # pragma: no cover
    def __getitem__(self, item): # pragma: no cover
        return self.tensor[item] # pragma: no cover
class TestStridedSlice(unittest.TestCase): # pragma: no cover
    def test_strided_slice(self): # pragma: no cover
        for tensor_type in STRIDED_SLICE_TYPES: # pragma: no cover
            with self.subTest(tensor_type=tensor_type, use_gpu=True): # pragma: no cover
                checker = StridedSliceChecker(self, StridedSliceChecker.REF_TENSOR, tensor_type=tensor_type) # pragma: no cover
                _ = checker[:, :, :] # pragma: no cover
                # Various ways of representing identity slice # pragma: no cover
                _ = checker[:, :, :] # pragma: no cover
                _ = checker[::, ::, ::] # pragma: no cover
                _ = checker[::1, ::1, ::1] # pragma: no cover
                # Not zero slice # pragma: no cover
                _ = checker[::1, ::5, ::2] # pragma: no cover
                # Reverse in each dimension independently # pragma: no cover
                _ = checker[::-1, :, :] # pragma: no cover
                _ = checker[:, ::-1, :] # pragma: no cover
                _ = checker[:, :, ::-1] # pragma: no cover
                ## negative index tests i.e. n-2 in first component # pragma: no cover
                _ = checker[-2::-1, :, ::1] # pragma: no cover
                # negative index tests i.e. n-2 in first component, non-unit stride # pragma: no cover
                _ = checker[-2::-1, :, ::2] # pragma: no cover
                # Check rank-0 examples # pragma: no cover
                checker2 = StridedSliceChecker(self, 5, tensor_type=tensor_type) # pragma: no cover
                _ = checker2[None] # pragma: no cover
                _ = checker2[...] # pragma: no cover
                _ = checker2[tuple()] # pragma: no cover

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
