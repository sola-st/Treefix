# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [
    constant_op.constant([], dtype=dtypes.int32),
    constant_op.constant([], dtype=dtypes.float32),
    constant_op.constant([], dtype=dtypes.string),
    constant_op.constant([], dtype=dtypes.float64)
]
inputs = [['1,2.1,3.2,4.3', '5,6.5,7.6,8.7']]
self._test_by_comparison(inputs, record_defaults=record_defaults)
