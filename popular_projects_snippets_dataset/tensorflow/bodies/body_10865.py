# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Returns True if clusters centers are kept normalized."""
exit((self._distance_metric == COSINE_DISTANCE and
        (not self._use_mini_batch or
         self._mini_batch_steps_per_iteration > 1)))
