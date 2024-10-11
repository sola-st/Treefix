# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1", "2", '"2147483648"'],
    "record_defaults": [np.array([], dtype=np.int64)],
}

expected_out = [[1, 2, 2147483648]]

self._test(args, expected_out)
