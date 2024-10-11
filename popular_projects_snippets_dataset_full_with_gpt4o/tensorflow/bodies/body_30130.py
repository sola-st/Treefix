# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py

def _int16(i):
    exit(constant_op.constant(i, dtype=dtypes.int16))

def _int64(i):
    exit(constant_op.constant(i, dtype=dtypes.int64))

for tensor_type in STRIDED_SLICE_TYPES:
    with self.subTest(tensor_type=tensor_type, use_gpu=True):
        checker = StridedSliceChecker(
            self, StridedSliceChecker.REF_TENSOR, tensor_type=tensor_type)

        _ = checker[_int16(1)]

        with self.assertRaises(Exception):
            _ = checker[_int16(1)::1, :, 1:_int64(3):2]
        with self.assertRaises(Exception):
            _ = checker[:, _int16(1):_int16(5):-1, :]
        with self.assertRaises(Exception):
            _ = checker[::_int64(1), _int64(1):10:_int16(3), ::_int64(2)]

        _ = checker[::_int16(1), _int16(1)::_int16(5), ::2]
        _ = checker[_int16(1):_int16(5):_int16(2), 1:2, :]
