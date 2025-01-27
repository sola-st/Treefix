# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reshape_op_test.py
with self.session():
    with self.test_scope():
        x = array_ops.zeros([50000, 50000], dtype=dtypes.bool)
        # Provide dimension larger than int32
        y = array_ops.reshape(x, [50000**2])
        self.assertEqual([50000**2], y.get_shape().as_list())
        # Even if first dimension is within int32, ensure we correctly go to
        # int64
        y = array_ops.reshape(x, [1, 50000**2])
        self.assertEqual([1, 50000**2], y.get_shape().as_list())
