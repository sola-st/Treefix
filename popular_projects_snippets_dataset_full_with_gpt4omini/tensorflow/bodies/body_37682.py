# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": [",1,", "0.2,3,bcd", '3.0,,"'],
    "record_defaults": [[1.0], [0], ["a"]],
    "use_quote_delim": False,
}

expected_out = [[1.0, 0.2, 3.0], [1, 3, 0], [b"a", b"bcd", b"\""]]

self._test(args, expected_out)
