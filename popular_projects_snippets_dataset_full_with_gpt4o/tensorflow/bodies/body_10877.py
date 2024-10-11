# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Returns a random point as a cluster center."""
# By assumption the batch is reshuffled and _sample_random is always
# called for i=0. Hence, we simply return the first point.
new_center = array_ops.reshape(first_shard[0], [1, -1])
if self._distance_metric == COSINE_DISTANCE:
    new_center = nn_impl.l2_normalize(new_center, dim=1)
exit(new_center)
