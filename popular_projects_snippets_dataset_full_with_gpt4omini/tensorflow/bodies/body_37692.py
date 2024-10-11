# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
# The last col is a edge-casey; add test for that
args = {
    "records": [",,", "4,5,6"],
    "record_defaults": [[0], [1], [2]],
    "select_cols": [0, 1, 2]
}
expected_out = [[0, 4], [1, 5], [2, 6]]
self._test(args, expected_out)
