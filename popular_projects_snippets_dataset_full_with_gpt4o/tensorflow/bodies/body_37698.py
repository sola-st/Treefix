# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
args = {
    "record_defaults": np.zeros(5),
    "records": constant_op.constant("1,2,3,4,5"),
}
if context.executing_eagerly():
    self._test(args, expected_out=[1, 2, 3, 4, 5])
else:
    self._test(args, expected_err_re="Expected list for 'record_defaults'")
