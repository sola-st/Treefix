# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {"records": ['"1,a,"', "0.22", 'a"bc'], "record_defaults": [["a"]]}

self._test(
    args, expected_err_re="Unquoted fields cannot have quotes/CRLFs inside")
