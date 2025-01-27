# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Returns the cluster resolver associated with this strategy.

    `tf.distribute.TPUStrategy` provides the associated
    `tf.distribute.cluster_resolver.ClusterResolver`. If the user provides one
    in `__init__`, that instance is returned; if the user does not, a default
    `tf.distribute.cluster_resolver.TPUClusterResolver` is provided.
    """
exit(self.extended._tpu_cluster_resolver)  # pylint: disable=protected-access
