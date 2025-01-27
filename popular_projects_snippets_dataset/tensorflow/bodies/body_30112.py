# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
from l3.Runtime import _l_
for tensor_type in STRIDED_SLICE_TYPES:
    _l_(18546)

    with self.subTest(tensor_type=tensor_type, use_gpu=True):
        _l_(18545)

        checker = StridedSliceChecker(
            self, StridedSliceChecker.REF_TENSOR, tensor_type=tensor_type)
        _l_(18530)
        _ = checker[:, :, :]
        _l_(18531)
        # Various ways of representing identity slice
        _ = checker[:, :, :]
        _l_(18532)
        _ = checker[::, ::, ::]
        _l_(18533)
        _ = checker[::1, ::1, ::1]
        _l_(18534)
        # Not zero slice
        _ = checker[::1, ::5, ::2]
        _l_(18535)
        # Reverse in each dimension independently
        _ = checker[::-1, :, :]
        _l_(18536)
        _ = checker[:, ::-1, :]
        _l_(18537)
        _ = checker[:, :, ::-1]
        _l_(18538)
        ## negative index tests i.e. n-2 in first component
        _ = checker[-2::-1, :, ::1]
        _l_(18539)
        # negative index tests i.e. n-2 in first component, non-unit stride
        _ = checker[-2::-1, :, ::2]
        _l_(18540)

        # Check rank-0 examples
        checker2 = StridedSliceChecker(self, 5, tensor_type=tensor_type)
        _l_(18541)
        _ = checker2[None]
        _l_(18542)
        _ = checker2[...]
        _l_(18543)
        _ = checker2[tuple()]
        _l_(18544)
