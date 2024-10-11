# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1,4", "2,5", "3,6"],
    "record_defaults": [1, 2],
}

expected_out = [[1, 2, 3], [4, 5, 6]]

self._test(args, expected_out)
