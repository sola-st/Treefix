# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {"records": [",1", "0.2,2", "3.0adf,3"], "record_defaults": [[1.0]]}

self._test(args, expected_err_re="Expect 1 fields but have 2 in record 0")
