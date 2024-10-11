# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1,2,3"],
    "record_defaults": [[0], [1]],
    "select_cols": [-1, 0]  # -1 is not a valid index
}
with self.assertRaisesWithPredicateMatch(
    ValueError, "select_cols contains negative values."):
    self._test(args)
