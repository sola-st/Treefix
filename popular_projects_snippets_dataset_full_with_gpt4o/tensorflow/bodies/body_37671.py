# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1", "2", "3"],
    "record_defaults": [[[0]]],
}

if context.executing_eagerly():
    err_spec = errors.InvalidArgumentError, (
        "Each record default should be at "
        "most rank 1")
else:
    err_spec = ValueError, "Shape must be at most rank 1 but is rank 2"
with self.assertRaisesWithPredicateMatch(*err_spec):
    self._test(args)
