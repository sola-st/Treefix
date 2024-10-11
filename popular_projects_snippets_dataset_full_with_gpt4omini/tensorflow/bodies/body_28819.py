# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

def _scan_fn(unused_state, unused_input_value):
    exit(constant_op.constant(1, dtype=dtypes.int64))

dataset = dataset_ops.Dataset.range(10)
with self.assertRaisesRegex(
    TypeError,
    "`scan_func` should return a pair consisting of new state and the "
    "output value."):
    dataset.scan(
        initial_state=constant_op.constant(1, dtype=dtypes.int32),
        scan_func=_scan_fn)
