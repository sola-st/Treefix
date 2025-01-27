# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_correctness_hd_sparse_training_test.py
if optimizer_name != 'sgd':
    self.skip_if_oss()
self._test_embedding(
    optimizer_name, training=True, sparse=True, is_high_dimensional=True)
