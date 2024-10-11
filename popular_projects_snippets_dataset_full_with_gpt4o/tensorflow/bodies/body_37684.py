# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": [",1", "0.2,3", "3.0,"],
    "record_defaults": [[1.0], np.array([], dtype=np.int32)]
}

self._test(
    args, expected_err_re="Field 1 is required but missing in record 2!")
