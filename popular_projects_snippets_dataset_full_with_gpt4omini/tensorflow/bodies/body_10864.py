# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Maps input to closest cluster and the score.

    Args:
      inputs: list of input Tensors.
      clusters: Tensor of cluster centers.

    Returns:
      List of tuple, where each value in tuple corresponds to a value in inp.
      The tuple has following three elements:
      all_scores: distance of each input to each cluster center.
      score: distance of each input to closest cluster center.
      cluster_idx: index of cluster center closest to the corresponding input.
    """
assert isinstance(inputs, list)
# Pairwise distances are used only by transform(). In all other cases, this
# sub-graph is not evaluated.
scores = self._distance_graph(inputs, clusters, self._distance_metric)
output = []
if (self._distance_metric == COSINE_DISTANCE and
    not self._clusters_l2_normalized()):
    # The cosine distance between normalized vectors x and y is the same as
    # 2 * squared_euclidean_distance. We are using this fact and reusing the
    # nearest_neighbors op.
    # TODO(ands): Support COSINE distance in nearest_neighbors and remove
    # this.
    with ops.colocate_with(clusters, ignore_existing=True):
        clusters = nn_impl.l2_normalize(clusters, axis=1)
for inp, score in zip(inputs, scores):
    with ops.colocate_with(inp, ignore_existing=True):
        (indices,
         distances) = gen_clustering_ops.nearest_neighbors(inp, clusters, 1)
        if self._distance_metric == COSINE_DISTANCE:
            distances *= 0.5
        output.append(
            (score, array_ops.squeeze(distances,
                                      [-1]), array_ops.squeeze(indices, [-1])))
exit(zip(*output))
