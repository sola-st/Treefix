# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {"records": [["1", "2"], ['""', "4"]], "record_defaults": [[5]]}
expected_out = [[[1, 2], [5, 4]]]

self._test(args, expected_out)
