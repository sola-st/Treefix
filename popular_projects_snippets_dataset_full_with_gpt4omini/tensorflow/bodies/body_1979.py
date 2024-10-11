# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py
for dtype in self.valid_dtypes:
    x = np.arange(1, 6).reshape([5]).astype(dtype)
    for axis_dtype in self.axis_dtypes():
        with self.session(), self.test_scope():
            p = array_ops.placeholder(x.dtype)
            axis = constant_op.constant(0, axis_dtype)
            math_ops.cumsum(p, axis).eval(feed_dict={p: x})
