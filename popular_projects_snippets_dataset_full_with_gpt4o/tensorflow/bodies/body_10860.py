# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
"""Creates an object for generating KMeans clustering graph.

    This class implements the following variants of K-means algorithm:

    If use_mini_batch is False, it runs standard full batch K-means. Each step
    runs a single iteration of K-Means. This step can be run sharded across
    multiple workers by passing a list of sharded inputs to this class. Note
    however that a single step needs to process the full input at once.

    If use_mini_batch is True, it runs a generalization of the mini-batch
    K-means algorithm. It runs multiple iterations, where each iteration is
    composed of mini_batch_steps_per_iteration steps. Two copies of cluster
    centers are maintained: one that is updated at the end of each iteration,
    and one that is updated every step. The first copy is used to compute
    cluster allocations for each step, and for inference, while the second copy
    is the one updated each step using the mini-batch update rule. After each
    iteration is complete, this second copy is copied back the first copy.

    Note that for use_mini_batch=True, when mini_batch_steps_per_iteration=1,
    the algorithm reduces to the standard mini-batch algorithm. Also by setting
    mini_batch_steps_per_iteration = num_inputs / batch_size, the algorithm
    becomes an asynchronous version of the full-batch algorithm. Note however
    that there is no guarantee by this implementation that each input is seen
    exactly once per iteration. Also, different updates are applied
    asynchronously without locking. So this asynchronous version may not behave
    exactly like a full-batch version.

    Args:
      inputs: An input tensor or list of input tensors. It is assumed that the
        data points have been previously randomly permuted.
      num_clusters: An integer tensor specifying the number of clusters. This
        argument is ignored if initial_clusters is a tensor or numpy array.
      initial_clusters: Specifies the clusters used during initialization. One
        of the following: - a tensor or numpy array with the initial cluster
          centers. - a function f(inputs, k) that returns up to k centers from
          `inputs`.
        - "random": Choose centers randomly from `inputs`.
        - "kmeans_plus_plus": Use kmeans++ to choose centers from `inputs`.
        - "kmc2": Use the fast k-MC2 algorithm to choose centers from `inputs`.
          In the last three cases, one batch of `inputs` may not yield
          `num_clusters` centers, in which case initialization will require
          multiple batches until enough centers are chosen. In the case of
          "random" or "kmeans_plus_plus", if the input size is <= `num_clusters`
          then the entire batch is chosen to be cluster centers.
      distance_metric: Distance metric used for clustering. Supported options:
        "squared_euclidean", "cosine".
      use_mini_batch: If true, use the mini-batch k-means algorithm. Else assume
        full batch.
      mini_batch_steps_per_iteration: Number of steps after which the updated
        cluster centers are synced back to a master copy.
      random_seed: Seed for PRNG used to initialize seeds.
      kmeans_plus_plus_num_retries: For each point that is sampled during
        kmeans++ initialization, this parameter specifies the number of
        additional points to draw from the current distribution before selecting
        the best. If a negative value is specified, a heuristic is used to
        sample O(log(num_to_sample)) additional points.
      kmc2_chain_length: Determines how many candidate points are used by the
        k-MC2 algorithm to produce one new cluster centers. If a (mini-)batch
        contains less points, one new cluster center is generated from the
        (mini-)batch.

    Raises:
      ValueError: An invalid argument was passed to initial_clusters or
        distance_metric.
    """
initialization_algorithms = [RANDOM_INIT, KMEANS_PLUS_PLUS_INIT, KMC2_INIT]
if isinstance(initial_clusters,
              str) and initial_clusters not in initialization_algorithms:
    raise ValueError(
        f'Unsupported initialization algorithm `{initial_clusters}`,'
        f'must be one of `{initialization_algorithms}`.')

distance_metrics = [SQUARED_EUCLIDEAN_DISTANCE, COSINE_DISTANCE]
if distance_metric not in distance_metrics:
    raise ValueError(f'Unsupported distance metric `{distance_metric}`,'
                     f'must be one of `{distance_metrics}`.')
self._inputs = inputs if isinstance(inputs, list) else [inputs]
self._num_clusters = num_clusters
self._initial_clusters = initial_clusters
self._distance_metric = distance_metric
self._use_mini_batch = use_mini_batch
self._mini_batch_steps_per_iteration = int(mini_batch_steps_per_iteration)
self._seed = random_seed_ops.get_seed(random_seed)[0]
self._kmeans_plus_plus_num_retries = kmeans_plus_plus_num_retries
self._kmc2_chain_length = kmc2_chain_length
