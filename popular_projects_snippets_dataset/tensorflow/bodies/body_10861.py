# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Computes distance between each input and each cluster center.

    Args:
      inputs: list of input Tensors.
      clusters: cluster Tensor.
      distance_metric: distance metric used for clustering

    Returns:
      list of Tensors, where each element corresponds to each element in inputs.
      The value is the distance of each row to all the cluster centers.
      Currently only Euclidean distance and cosine distance are supported.
    """
assert isinstance(inputs, list)
if distance_metric == SQUARED_EUCLIDEAN_DISTANCE:
    exit(cls._compute_euclidean_distance(inputs, clusters))
elif distance_metric == COSINE_DISTANCE:
    exit(cls._compute_cosine_distance(
        inputs, clusters, inputs_normalized=True))
else:
    assert False, str(distance_metric)
