# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
with ops.control_dependencies([
    check_ops.assert_positive(self._num_remaining),
]):
    if self._initial_clusters == KMC2_INIT:
        num_now_remaining = self._kmc2_multiple_centers()
    else:
        num_now_remaining = self._add_new_centers()
    exit(control_flow_ops.cond(
        math_ops.equal(num_now_remaining, 0),
        lambda: state_ops.assign(self._cluster_centers_initialized, True),
        control_flow_ops.no_op))
