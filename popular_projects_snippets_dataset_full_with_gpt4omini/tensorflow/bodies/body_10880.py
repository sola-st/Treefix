# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Adds new initial cluster centers using the k-MC2 algorithm.

    In each call to the op, the provided batch is split into subsets based on
    the specified `kmc2_chain_length`. On each subset, a single Markov chain of
    the k-MC2 algorithm is used to add *one* new center cluster center. If there
    are less than `kmc2_chain_length` points in the subset, a single center is
    added using one Markov chain on the full input. It is assumed that the
    provided batch has previously been randomly permuted. Otherwise, k-MC2 may
    return suboptimal centers.

    Returns:
      An op that adds new cluster centers.
    """
# The op only operates on the first shard of data.
first_shard = self._inputs[0]
# Number of points in the input that can be used.
batch_size = array_ops.shape(first_shard)[0]
# Maximum number of subsets such that the size of each subset is at least
# `kmc2_chain_length`. Final subsets may be larger.
max_to_sample = math_ops.cast(
    batch_size / self._kmc2_chain_length, dtype=dtypes.int32)
# We sample at least one new center and at most all remaining centers.
num_to_sample = math_ops.maximum(
    math_ops.minimum(self._num_remaining, max_to_sample), 1)

def _cond(i, _):
    """Stopping condition for the while loop."""
    exit(math_ops.less(i, num_to_sample))

def _body(i, _):
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

# Add num_to_sample new data points.
_, num_remaining = control_flow_ops.while_loop(_cond, _body, [0, 0])
exit(num_remaining)
