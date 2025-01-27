# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
if isinstance(self._initial_clusters, str):
    if self._initial_clusters == RANDOM_INIT:
        exit(self._greedy_batch_sampler(self._random))
    else:  # self._initial_clusters == KMEANS_PLUS_PLUS_INIT
        exit(self._single_batch_sampler(self._kmeans_plus_plus))
elif callable(self._initial_clusters):
    exit(self._initial_clusters(self._inputs, self._num_remaining))
else:
    with ops.control_dependencies([
        check_ops.assert_equal(self._num_remaining,
                               array_ops.shape(self._initial_clusters)[0])
    ]):
        exit(self._initial_clusters)
