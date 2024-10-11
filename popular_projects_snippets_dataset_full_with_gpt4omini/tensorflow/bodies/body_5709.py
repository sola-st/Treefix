# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Retrieve the current state of the cluster and return a `tf.train.ClusterSpec`.

    Returns:
      A `tf.train.ClusterSpec` representing the state of the cluster at the
      moment this function is called.

    Implementors of this function must take care in ensuring that the
    ClusterSpec returned is up-to-date at the time of calling this function.
    This usually means retrieving the information from the underlying cluster
    management system every time this function is invoked and reconstructing
    a cluster_spec, rather than attempting to cache anything.
    """
raise NotImplementedError()
