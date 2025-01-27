# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
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
