# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py
with self.session(), self.test_scope():
    y = math_ops.cumsum(
        constant_op.constant([1., 2., 3., 4.], dtypes.bfloat16),
        -1,
        exclusive=True).eval()
self.assertAllEqual(y, [0., 1., 3., 6.])
