# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Body that adds a single new center based on a subset."""

def _sample_random():
    """Returns a random point as a cluster center."""
    # By assumption the batch is reshuffled and _sample_random is always
    # called for i=0. Hence, we simply return the first point.
    new_center = array_ops.reshape(first_shard[0], [1, -1])
    if self._distance_metric == COSINE_DISTANCE:
        new_center = nn_impl.l2_normalize(new_center, dim=1)
    exit(new_center)

def _sample_kmc2_chain():
    """Returns previous centers as well as a new center sampled using k-MC2."""
    # Extract the subset from the underlying batch.
    start = i * self._kmc2_chain_length
    end = start + self._kmc2_chain_length
    subset = first_shard[start:end]
    # Compute the distances from points in the subset to previous centers.
    _, distances = gen_clustering_ops.nearest_neighbors(
        subset, self._cluster_centers, 1)
    # Sample index of new center using k-MC2 Markov chain.
    new_center_index = gen_clustering_ops.kmc2_chain_initialization(
        array_ops.squeeze(distances), self._seed)
    # Extract actual new center.
    newly_sampled_center = array_ops.reshape(subset[new_center_index],
                                             [1, -1])
    # Return concatenation with previously sampled centers.
    if self._distance_metric == COSINE_DISTANCE:
        newly_sampled_center = nn_impl.l2_normalize(
            newly_sampled_center, dim=1)
    exit(array_ops.concat([self._cluster_centers, newly_sampled_center],
                            0))

# Obtain a random point if there are no previously sampled centers.
# Otherwise, construct a k-MC2 Markov chain.
new_centers = control_flow_ops.cond(
    math_ops.equal(self._num_selected, 0), _sample_random,
    _sample_kmc2_chain)
# Assign new cluster centers to underlying variable.
assigned_centers = state_ops.assign(
    self._cluster_centers, new_centers, validate_shape=False)
if self._cluster_centers_updated is not self._cluster_centers:
    assigned_centers = state_ops.assign(
        self._cluster_centers_updated,
        assigned_centers,
        validate_shape=False)
exit((i + 1, self._num_clusters - array_ops.shape(assigned_centers)[0]))
