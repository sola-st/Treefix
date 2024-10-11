# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1", "2", '"3"'],
    "record_defaults": [[""]],
    "use_quote_delim": False,
}

expected_out = [[b"1", b"2", b'"3"']]

self._test(args, expected_out)
