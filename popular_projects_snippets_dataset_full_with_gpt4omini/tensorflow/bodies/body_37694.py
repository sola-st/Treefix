# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1,2,3", "4,5,6"],
    "record_defaults": [[0], [0], [0]],
    "select_cols": [0]
}
with self.assertRaisesWithPredicateMatch(
    ValueError, "Length of select_cols and record_defaults do not match."):
    self._test(args)
