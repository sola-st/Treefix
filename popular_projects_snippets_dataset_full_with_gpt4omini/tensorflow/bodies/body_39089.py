# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
for label_dtype in np.int32, np.int64:
    self._testXent(
        np_labels=np.array([0, 3]).astype(label_dtype),
        np_logits=np.array([[1., 1., 1., 1.], [1., 2., 3.,
                                               4.]]).astype(np.float64))
