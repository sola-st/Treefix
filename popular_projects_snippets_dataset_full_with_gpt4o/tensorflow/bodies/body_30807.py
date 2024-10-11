# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softsign_op_test.py
with self.cached_session():
    with self.assertRaisesRegex(
        TypeError,
        "'features' has DataType int32 not in list of allowed values"):
        nn_ops.softsign(constant_op.constant(7)).eval()
