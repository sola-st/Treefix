# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with self.session(use_gpu=False) as sess:
    sp_input = array_ops.sparse_placeholder(dtype=dtypes.int32)
    new_shape = np.array([3, 6, 7], dtype=np.int64)
    sp_output = sparse_ops.sparse_reset_shape(sp_input, new_shape)

    output = sess.run(sp_output,
                      feed_dict={sp_input: self._SparseTensorValue_2x5x6()})

    self.assertAllEqual(output.indices, [[0, 0, 0], [0, 1, 0], [0, 1, 3],
                                         [1, 1, 4], [1, 3, 2], [1, 3, 3]])
    self.assertAllEqual(output.values, [0, 10, 13, 14, 32, 33])
    self.assertAllEqual(output.dense_shape, [3, 6, 7])
