# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Creates an op for training for full batch case.

    Args:
      inputs: list of input Tensors.
      num_clusters: an integer Tensor providing the number of clusters.
      cluster_idx_list: A vector (or list of vectors). Each element in the
        vector corresponds to an input row in 'inp' and specifies the cluster id
        corresponding to the input.
      cluster_centers: Tensor Ref of cluster centers.

    Returns:
      An op for doing an update of mini-batch k-means.
    """
cluster_sums = []
cluster_counts = []
epsilon = constant_op.constant(1e-6, dtype=inputs[0].dtype)
for inp, cluster_idx in zip(inputs, cluster_idx_list):
    with ops.colocate_with(inp, ignore_existing=True):
        cluster_sums.append(
            math_ops.unsorted_segment_sum(inp, cluster_idx, num_clusters))
        cluster_counts.append(
            math_ops.unsorted_segment_sum(
                array_ops.reshape(
                    array_ops.ones(
                        array_ops.reshape(array_ops.shape(inp)[0], [-1])),
                    [-1, 1]), cluster_idx, num_clusters))
with ops.colocate_with(cluster_centers, ignore_existing=True):
    new_clusters_centers = math_ops.add_n(cluster_sums) / (
        math_ops.cast(math_ops.add_n(cluster_counts), cluster_sums[0].dtype) +
        epsilon)
    if self._clusters_l2_normalized():
        new_clusters_centers = nn_impl.l2_normalize(new_clusters_centers, dim=1)
exit(state_ops.assign(cluster_centers, new_clusters_centers))
