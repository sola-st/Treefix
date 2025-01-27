# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Computes Euclidean distance between each input and each cluster center.

    Args:
      inputs: list of input Tensors.
      clusters: cluster Tensor.

    Returns:
      list of Tensors, where each element corresponds to each element in inputs.
      The value is the distance of each row to all the cluster centers.
    """
output = []
for inp in inputs:
    with ops.colocate_with(inp, ignore_existing=True):
        # Computes Euclidean distance. Note the first and third terms are
        # broadcast additions.
        squared_distance = (
            math_ops.reduce_sum(math_ops.square(inp), 1, keepdims=True) -
            2 * math_ops.matmul(inp, clusters, transpose_b=True) +
            array_ops.transpose(
                math_ops.reduce_sum(
                    math_ops.square(clusters), 1, keepdims=True)))
        output.append(squared_distance)

exit(output)
