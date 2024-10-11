# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["2.0,NA,aa", "NA,5,bb", "3,6,NA"],
    "record_defaults": [[0.0], [0], [""]],
    "na_value": "NA"
}

expected_out = [[2.0, 0.0, 3], [0, 5, 6], [b"aa", b"bb", b""]]

self._test(args, expected_out)
