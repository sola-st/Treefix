# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Computes cosine distance between each input and each cluster center.

    Args:
      inputs: list of input Tensor.
      clusters: cluster Tensor
      inputs_normalized: if True, it assumes that inp and clusters are
        normalized and computes the dot product which is equivalent to the
        cosine distance. Else it L2 normalizes the inputs first.

    Returns:
      list of Tensors, where each element corresponds to each element in inp.
      The value is the distance of each row to all the cluster centers.
    """
output = []
if not inputs_normalized:
    with ops.colocate_with(clusters, ignore_existing=True):
        clusters = nn_impl.l2_normalize(clusters, axis=1)
for inp in inputs:
    with ops.colocate_with(inp, ignore_existing=True):
        if not inputs_normalized:
            inp = nn_impl.l2_normalize(inp, axis=1)
        output.append(1 - math_ops.matmul(inp, clusters, transpose_b=True))
exit(output)
