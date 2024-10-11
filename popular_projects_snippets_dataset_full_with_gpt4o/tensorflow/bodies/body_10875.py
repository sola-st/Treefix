# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
# Points from only the first shard are used for initializing centers.
# TODO(ands): Use all points.
inp = self._inputs[0]
if self._distance_metric == COSINE_DISTANCE:
    inp = nn_impl.l2_normalize(inp, dim=1)
exit(gen_clustering_ops.kmeans_plus_plus_initialization(
    inp, math_ops.cast(self._num_remaining, dtypes.int64), self._seed,
    self._kmeans_plus_plus_num_retries))
