# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
# Eigenvectors corresponding to a cluster of close eigenvalues are not
# uniquely defined, but the subspace they span is. To avoid numerical
# instability, we explicitly mutually orthogonalize such eigenvectors
# after each step of inverse iteration. It is customary to use
# modified Gram-Schmidt for this, but this is not very efficient
# on some platforms, so here we defer to the QR decomposition in
# TensorFlow.
def orthogonalize_cluster(cluster_idx, eigenvectors):
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

_, eigenvectors = control_flow_ops.while_loop(
    lambda i, ev: math_ops.less(i, num_clusters),
    orthogonalize_cluster, [0, eigenvectors])
exit(eigenvectors)
