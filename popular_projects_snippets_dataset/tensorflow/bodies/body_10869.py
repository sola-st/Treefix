# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
# Note that there is a race condition here, so we do a best effort
# updates here. We reset update_in_steps first so that other workers
# don't duplicate the updates. Also we update cluster_center_vars
# before resetting total_counts to avoid large updates to
# cluster_centers_updated based on partially updated
# cluster_center_vars.
with ops.control_dependencies([
    state_ops.assign(update_in_steps,
                     self._mini_batch_steps_per_iteration - 1)
]):
    with ops.colocate_with(
        cluster_centers_updated, ignore_existing=True):
        if self._distance_metric == COSINE_DISTANCE:
            cluster_centers = nn_impl.l2_normalize(
                cluster_centers_updated, dim=1)
        else:
            cluster_centers = cluster_centers_updated
    with ops.colocate_with(cluster_centers_var, ignore_existing=True):
        with ops.control_dependencies(
            [state_ops.assign(cluster_centers_var, cluster_centers)]):
            with ops.colocate_with(None, ignore_existing=True):
                with ops.control_dependencies([
                    state_ops.assign(total_counts,
                                     array_ops.zeros_like(total_counts))
                ]):
                    exit(array_ops.identity(update_in_steps))
