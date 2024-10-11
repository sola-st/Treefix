# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
labels = np.array([[0., 0., 0., 1.], [0., .5, .5, 0.]]).astype(np.float16)
logits = np.array([[1., 1., 1., 1.], [1., 2., 3., 4.]]).astype(np.float16)
self._testXent2D(labels, logits)
