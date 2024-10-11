# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ['"1.0"', '"ab , c"', '"a\nbc"', '"ab""c"', " abc "],
    "record_defaults": [["1"]]
}

expected_out = [[b"1.0", b"ab , c", b"a\nbc", b'ab"c', b" abc "]]

self._test(args, expected_out)
