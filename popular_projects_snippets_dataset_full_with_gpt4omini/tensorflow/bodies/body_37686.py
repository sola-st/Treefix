# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1", "9999999999999999999999999", "3"],
    "record_defaults": [[1]]
}

self._test(
    args, expected_err_re="Field 0 in record 1 is not a valid int32: ")
