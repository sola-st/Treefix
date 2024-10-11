# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Adds some centers and returns the number of centers remaining."""
new_centers = self._choose_initial_centers()
if self._distance_metric == COSINE_DISTANCE:
    new_centers = nn_impl.l2_normalize(new_centers, dim=1)
# If cluster_centers is empty, it doesn't have the right shape for concat.
all_centers = control_flow_ops.cond(
    math_ops.equal(self._num_selected, 0), lambda: new_centers,
    lambda: array_ops.concat([self._cluster_centers, new_centers], 0))
# TODO(ccolby): De-dupe all_centers?
a = state_ops.assign(
    self._cluster_centers, all_centers, validate_shape=False)
if self._cluster_centers_updated is not self._cluster_centers:
    a = state_ops.assign(
        self._cluster_centers_updated, a, validate_shape=False)
exit(self._num_clusters - array_ops.shape(a)[0])
