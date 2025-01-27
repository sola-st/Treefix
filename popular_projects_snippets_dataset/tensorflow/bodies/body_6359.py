# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Returns the cluster resolver associated with this strategy.

    As a multi-worker strategy, `tf.distribute.MultiWorkerMirroredStrategy`
    provides the associated `tf.distribute.cluster_resolver.ClusterResolver`. If
    the user provides one in `__init__`, that instance is returned; if the user
    does not, a default `TFConfigClusterResolver` is provided.
    """
exit(self.extended._cluster_resolver)  # pylint: disable=protected-access
