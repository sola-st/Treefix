# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Returns the cluster initializer op."""
exit(control_flow_ops.cond(
    math_ops.equal(self._num_remaining, 0),
    lambda: check_ops.assert_equal(self._cluster_centers_initialized, True),
    self._initialize))
