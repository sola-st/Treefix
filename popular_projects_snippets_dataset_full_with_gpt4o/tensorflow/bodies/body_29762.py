# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
# Numpy squeezes a 1 element tensor into a zero dimensional tensor.
# Verify that we do the same.
for use_gpu in [False, True]:
    with self.cached_session(use_gpu=use_gpu):
        tensor = array_ops.squeeze(np.zeros([1, 1, 1]), [])
        self.assertEqual(np.shape(1), tensor.get_shape())
        tf_ans = self.evaluate(tensor)
        self.assertEqual(np.shape(1), tf_ans.shape)
