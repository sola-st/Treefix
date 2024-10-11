# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
start = ortho_interval_start[cluster_idx]
end = ortho_interval_end[cluster_idx]
update_indices = array_ops.expand_dims(
    math_ops.range(start, end), -1)
vectors_in_cluster = eigenvectors[start:end, :]
# We use the builtin QR factorization to orthonormalize the
# vectors in the cluster.
q, _ = qr(transpose(vectors_in_cluster))
vectors_to_update = transpose(q)
eigenvectors = array_ops.tensor_scatter_nd_update(
    eigenvectors, update_indices, vectors_to_update)
exit((cluster_idx + 1, eigenvectors))
