# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session():
    v = array_ops.placeholder(dtype=dtypes_lib.float32)
    with self.assertRaisesOpError("diagonal must be at least 1-dim"):
        array_ops.matrix_diag(v).eval(feed_dict={v: 0.0})
