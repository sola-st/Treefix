# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Creates an op for training for mini batch case.

    Args:
      inputs: list of input Tensors.
      cluster_idx_list: A vector (or list of vectors). Each element in the
        vector corresponds to an input row in 'inp' and specifies the cluster id
        corresponding to the input.
      cluster_centers: Tensor Ref of cluster centers.
      total_counts: Tensor Ref of cluster counts.

    Returns:
      An op for doing an update of mini-batch k-means.
    """
update_ops = []
for inp, cluster_idx in zip(inputs, cluster_idx_list):
    with ops.colocate_with(inp, ignore_existing=True):
        assert total_counts is not None
        cluster_idx = array_ops.reshape(cluster_idx, [-1])
        # Dedupe the unique ids of cluster_centers being updated so that updates
        # can be locally aggregated.
        unique_ids, unique_idx = array_ops.unique(cluster_idx)
        num_unique_cluster_idx = array_ops.size(unique_ids)
        # Fetch the old values of counts and cluster_centers.
        with ops.colocate_with(total_counts, ignore_existing=True):
            old_counts = array_ops.gather(total_counts, unique_ids)
        # TODO(agarwal): This colocation seems to run into problems. Fix it.
        with ops.colocate_with(cluster_centers, ignore_existing=True):
            old_cluster_centers = array_ops.gather(cluster_centers, unique_ids)
        # Locally aggregate the increment to counts.
        count_updates = math_ops.unsorted_segment_sum(
            array_ops.ones_like(unique_idx, dtype=total_counts.dtype),
            unique_idx, num_unique_cluster_idx)
        # Locally compute the sum of inputs mapped to each id.
        # For a cluster with old cluster value x, old count n, and with data
        # d_1,...d_k newly assigned to it, we recompute the new value as
        # \\(x += (sum_i(d_i) - k * x) / (n + k)\\).
        # Compute \\(sum_i(d_i)\\), see comment above.
        cluster_center_updates = math_ops.unsorted_segment_sum(
            inp, unique_idx, num_unique_cluster_idx)
        # Shape to enable broadcasting count_updates and learning_rate to inp.
        # It extends the shape with 1's to match the rank of inp.
        broadcast_shape = array_ops.concat([
            array_ops.reshape(num_unique_cluster_idx, [1]),
            array_ops.ones(
                array_ops.reshape(array_ops.rank(inp) - 1, [1]),
                dtype=dtypes.int32)
        ], 0)
        # Subtract k * x, see comment above.
        cluster_center_updates -= math_ops.cast(
            array_ops.reshape(count_updates, broadcast_shape),
            inp.dtype) * old_cluster_centers
        learning_rate = math_ops.reciprocal(
            math_ops.cast(old_counts + count_updates, inp.dtype))
        learning_rate = array_ops.reshape(learning_rate, broadcast_shape)
        # scale by 1 / (n + k), see comment above.
        cluster_center_updates *= learning_rate
        # Apply the updates.
    update_counts = state_ops.scatter_add(total_counts, unique_ids,
                                          count_updates)
    update_cluster_centers = state_ops.scatter_add(cluster_centers,
                                                   unique_ids,
                                                   cluster_center_updates)
    update_ops.extend([update_counts, update_cluster_centers])
exit(control_flow_ops.group(*update_ops))
