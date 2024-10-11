# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Creates an op factory.

    Args:
      inputs: See KMeans constructor.
      num_clusters: An integer Tensor providing the number of clusters.
      initial_clusters: See KMeans constructor.
      distance_metric: See KMeans constructor.
      random_seed: See KMeans constructor.
      kmeans_plus_plus_num_retries: See KMeans constructor.
      kmc2_chain_length: See KMeans constructor.
      cluster_centers: The TF variable holding the initial centers. It may
        already contain some centers when the op is executed.
      cluster_centers_updated: A second TF variable to hold a copy of the
        initial centers, used for full-batch mode. In mini-batch mode,
        cluster_centers_updated is the same variable as cluster_centers.
      cluster_centers_initialized: A boolean TF variable that will be set to
        true when all the initial centers have been chosen.
    """
# All of these instance variables are constants.
self._inputs = inputs
self._num_clusters = num_clusters
self._initial_clusters = initial_clusters
self._distance_metric = distance_metric
self._seed = random_seed
self._kmeans_plus_plus_num_retries = kmeans_plus_plus_num_retries
self._kmc2_chain_length = kmc2_chain_length
self._cluster_centers = cluster_centers
self._cluster_centers_updated = cluster_centers_updated
self._cluster_centers_initialized = cluster_centers_initialized

self._num_selected = array_ops.shape(self._cluster_centers)[0]
self._num_remaining = self._num_clusters - self._num_selected
self._num_data = math_ops.add_n(
    [array_ops.shape(i)[0] for i in self._inputs])
