# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
labels = np.array([[0., 0., 0., 1.]]).astype(np.float16)
logits = np.array([[1., 1., 1., 1.], [1., 2., 3., 4.]]).astype(np.float16)
self._testXent2D(labels, logits, with_placeholders=True)
labels = np.array([[1.]]).astype(np.float16)
logits = np.array([[1.], [2.]]).astype(np.float16)
self._testXent2D(labels, logits, with_placeholders=True)
labels = np.array([[0.], [2.], [0.25]]).astype(np.float16)
logits = np.array([[1., 1., 1., 1.], [1., 2., 3., 4.],
                   [1., 2., 3., 4.]]).astype(np.float16)
self._testXent2D(
    labels,
    logits,
    with_placeholders=True,
    expected_gradient=uniform_labels_gradient)
