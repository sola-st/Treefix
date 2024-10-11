# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session():
    v = array_ops.placeholder(dtype=dtypes_lib.float32)
    with self.assertRaisesOpError("input must be at least 2-dim"):
        array_ops.matrix_set_diag(v, [v]).eval(feed_dict={v: 0.0})
    with self.assertRaisesOpError("diagonal must be at least 1-dim"):
        array_ops.matrix_set_diag([[v]], v).eval(feed_dict={v: 0.0})

    d = array_ops.placeholder(dtype=dtypes_lib.float32)
    with self.assertRaisesOpError(
        "first dimensions of diagonal don't match"):
        array_ops.matrix_set_diag(v, d).eval(feed_dict={
            v: np.zeros((2, 3, 3)),
            d: np.ones((2, 4))
        })
