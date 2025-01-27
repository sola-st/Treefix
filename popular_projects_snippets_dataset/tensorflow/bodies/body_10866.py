# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Creates variables.

    Args:
      num_clusters: an integer Tensor providing the number of clusters.

    Returns:
      Tuple with following elements:
      - cluster_centers: a Tensor for storing cluster centers
      - cluster_centers_initialized: bool Variable indicating whether clusters
            are initialized.
      - cluster_counts: a Tensor for storing counts of points assigned to this
            cluster. This is used by mini-batch training.
      - cluster_centers_updated: Tensor representing copy of cluster centers
            that are updated every step.
      - update_in_steps: numbers of steps left before we sync
            cluster_centers_updated back to cluster_centers.
    """
init_value = array_ops.placeholder_with_default([], shape=None)
cluster_centers = variable_scope.variable(
    init_value, name=CLUSTERS_VAR_NAME, validate_shape=False)
cluster_centers_initialized = variable_scope.variable(
    False, dtype=dtypes.bool, name='initialized')

if self._use_mini_batch and self._mini_batch_steps_per_iteration > 1:
    # Copy of cluster centers actively updated each step according to
    # mini-batch update rule.
    cluster_centers_updated = variable_scope.variable(
        init_value, name='clusters_updated', validate_shape=False)
    # How many steps till we copy the updated clusters to cluster_centers.
    update_in_steps = variable_scope.variable(
        self._mini_batch_steps_per_iteration,
        dtype=dtypes.int64,
        name='update_in_steps')
    # Count of points assigned to cluster_centers_updated.
    cluster_counts = variable_scope.variable(
        array_ops.zeros([num_clusters], dtype=dtypes.int64))
else:
    cluster_centers_updated = cluster_centers
    update_in_steps = None
    cluster_counts = (
        variable_scope.variable(
            array_ops.ones([num_clusters], dtype=dtypes.int64))
        if self._use_mini_batch else None)
exit((cluster_centers, cluster_centers_initialized, cluster_counts,
        cluster_centers_updated, update_in_steps))
