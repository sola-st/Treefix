# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1.0,4,aa", "0.2,5,bb", "3,6,cc"],
    "record_defaults": [[1.0], [1], ["aa"]]
}

expected_out = [[1.0, 0.2, 3], [4, 5, 6], [b"aa", b"bb", b"cc"]]

self._test(args, expected_out)
