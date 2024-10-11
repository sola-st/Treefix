# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {"records": '1,""', "record_defaults": [[3], [4]]}

expected_out = [1, 4]

self._test(args, expected_out)
