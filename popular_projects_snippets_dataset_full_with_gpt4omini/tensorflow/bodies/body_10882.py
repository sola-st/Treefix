# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
# Enforce that there are at least as many data points as centers
# remaining. This gives the provided sampler the chance to select all
# remaining centers from a single batch.
with ops.control_dependencies(
    [check_ops.assert_greater_equal(self._num_data, self._num_remaining)]):
    exit(sampler())
