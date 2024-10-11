# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
with self.cached_session(use_gpu=False) as sess:
    matrix = np.random.rand(256) * 10
    tensor = constant_op.constant(matrix, dtypes.uint8, shape=matrix.shape)
    tensor_one_hot = array_ops.one_hot(tensor, depth=10, axis=0)
    self.assertEqual(sess.run(tensor_one_hot).shape, (10, 256))
