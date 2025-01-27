# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_correctness_hd_ragged_forward_test.py
if optimizer_name != 'sgd':
    self.skip_if_oss()
self._test_embedding(
    optimizer_name, training=False, sparse=False, is_high_dimensional=True)
