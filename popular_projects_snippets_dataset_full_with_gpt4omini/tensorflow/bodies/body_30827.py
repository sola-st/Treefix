# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
labels = np.array([[[0., 0., 0., 1.], [0., 1., 0., 0.]],
                   [[0., 0.5, 0.5, 0.], [0.5, 0.5, 0., 0.]],
                   [[0., 1., 0., 0.], [0., 0., 1., 0.]]]).astype(np.float32)
logits = np.array([[[1., 1., 1., 1.], [1., 2., 3., 4.]],
                   [[2., 3., 4., 5.], [6., 7., 8., 9.]],
                   [[5., 4., 3., 2.], [1., 2., 3., 4.]]]).astype(np.float32)
self._testXentND(labels, logits, dim=0)
self._testXentND(labels, logits, dim=1)
self._testXentND(labels, logits, dim=-1)
