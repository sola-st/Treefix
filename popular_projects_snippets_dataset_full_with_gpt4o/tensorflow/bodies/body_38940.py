# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
sp_input = array_ops.sparse_placeholder(dtype=dtypes.int32)
with self.session(use_gpu=False) as sess:
    new_shape = np.array([3, 7, 5], dtype=np.int64)
    out = sparse_ops.sparse_reset_shape(sp_input, new_shape)

    with self.assertRaisesOpError("x <= y did not hold element-wise"):
        sess.run(out, feed_dict={sp_input: self._SparseTensorValue_2x5x6()})
