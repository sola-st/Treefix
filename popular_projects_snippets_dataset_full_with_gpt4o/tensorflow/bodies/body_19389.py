# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_correctness_sparse_forward_test.py
if optimizer_name != 'sgd':
    self.skip_if_oss()
self._test_embedding(
    optimizer_name, training=False, sparse=True, is_high_dimensional=False)
