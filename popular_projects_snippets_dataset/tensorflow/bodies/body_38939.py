# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with self.session(use_gpu=False) as sess:
    sp_input = self._SparseTensor_2x5x6()
    new_shape = array_ops.placeholder(dtype=dtypes.int32)
    out = sparse_ops.sparse_reset_shape(sp_input, new_shape)

    with self.assertRaisesOpError("x <= y did not hold element-wise"):
        sess.run(out, feed_dict={new_shape: [3, 7, 5]})
