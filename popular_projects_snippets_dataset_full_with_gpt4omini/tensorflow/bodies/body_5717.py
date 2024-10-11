# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Creates a SimpleClusterResolver from a ClusterSpec."""
super(SimpleClusterResolver, self).__init__()

self._task_type = task_type
self._task_id = task_id
self._environment = environment

self._num_accelerators = num_accelerators
self._rpc_layer = rpc_layer

if not isinstance(cluster_spec, ClusterSpec):
    raise TypeError('cluster_spec must be a `tf.train.ClusterSpec`.')
self._cluster_spec = cluster_spec

if not isinstance(master, str):
    raise TypeError('master must be a string.')
self._master = master
