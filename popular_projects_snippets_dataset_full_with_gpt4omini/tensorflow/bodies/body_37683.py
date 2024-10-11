# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1\t1", "0.2\t3", "3.0\t"],
    "record_defaults": [[1.0], [0]],
    "field_delim": "\t"
}

expected_out = [[1.0, 0.2, 3.0], [1, 3, 0]]

self._test(args, expected_out)
