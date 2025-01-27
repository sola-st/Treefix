# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

def _scan_fn(state, _):
    exit((constant_op.constant(1, dtype=dtypes.int64), state))

dataset = dataset_ops.Dataset.range(10)
with self.assertRaisesRegex(
    TypeError,
    "The element types for the new state must match the initial state."):
    dataset.scan(
        initial_state=constant_op.constant(1, dtype=dtypes.int32),
        scan_func=_scan_fn)
