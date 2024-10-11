# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1,2,3"],
    "record_defaults": [[0], [1]],
    "select_cols": [0, 3]  # 3 is not a valid index
}
# Only successfully parses one of the columns
self._test(args, expected_err_re="Expect 2 fields but have 1 in record 0")
