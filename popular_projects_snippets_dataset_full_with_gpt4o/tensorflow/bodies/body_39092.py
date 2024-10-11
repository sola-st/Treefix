# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
self._testXent(
    np_labels=np.zeros((0,), dtype=np.int32), np_logits=np.zeros((0, 3)))
