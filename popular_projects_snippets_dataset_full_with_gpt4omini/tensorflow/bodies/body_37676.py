# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": ["1.0", "-1.79e+308", '"1.79e+308"'],
    "record_defaults": [np.array([], dtype=np.double)],
}

expected_out = [[1.0, -1.79e+308, 1.79e+308]]

self._test(args, expected_out)
