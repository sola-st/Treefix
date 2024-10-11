# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "records": [",1", "0.2,2", "3.0adf,3"],
    "record_defaults": [[1.0], np.array([], dtype=np.int32)]
}

self._test(
    args, expected_err_re="Field 0 in record 2 is not a valid float: ")
