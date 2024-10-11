# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["\""],
    "record_defaults": [["default"]],
}

self._test(
    args, expected_err_re="Quoted field has to end with quote followed.*")
