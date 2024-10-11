# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
"""Tests cast(x) to different tf."""
if use_gpu:
    type_list = [
        np.float32, np.float64, np.int64, np.complex64, np.complex128
    ]
else:
    type_list = [
        np.float32, np.float64, np.int32, np.int64, np.complex64,
        np.complex128
    ]
for from_type in type_list:
    for to_type in type_list:
        self._test(x.astype(from_type), to_type, use_gpu)

self._test(x.astype(np.bool_), np.float32, use_gpu)
self._test(x.astype(np.uint8), np.float32, use_gpu)
if not use_gpu:
    self._test(x.astype(np.bool_), np.int32, use_gpu)
    self._test(x.astype(np.int32), np.int32, use_gpu)
