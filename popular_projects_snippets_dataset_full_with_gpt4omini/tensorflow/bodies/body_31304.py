# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test.py
for dtype in np.float16, np.float32:
    np_features = np.array([[[1., 1., 1., 1.]], [[1., 2., 3.,
                                                  4.]]]).astype(dtype)
    np_labels = np.array([[[0., 0., 0., 1.]], [[0., .5, .5,
                                                0.]]]).astype(dtype)
    self.assertRaisesRegex(ValueError, "rank 2, but is rank 3",
                           gen_nn_ops.softmax_cross_entropy_with_logits,
                           np_features, np_labels)
