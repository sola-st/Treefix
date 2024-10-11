# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": [",,", "4,5,6"],
    "record_defaults": [[1], [2]],
    "select_cols": [0, 1]
}
expected_out = [[1, 4], [2, 5]]
self._test(args, expected_out)
