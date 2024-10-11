# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with self.session(use_gpu=False) as sess:
    new_shape = array_ops.placeholder(dtype=dtypes.int64)
    sp_input = self._SparseTensor_2x5x6()
    out = sparse_ops.sparse_reset_shape(sp_input, new_shape)

    with self.assertRaisesOpError("x == y did not hold element-wise"):
        sess.run(out, feed_dict={new_shape: np.array([3, 7], dtype=np.int64)})
