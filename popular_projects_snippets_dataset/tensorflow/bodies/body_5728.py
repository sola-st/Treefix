# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Initializes a UnionClusterResolver with other ClusterResolvers.

    Args:
      *args: `ClusterResolver` objects to be unionized.
      **kwargs:
        rpc_layer - (Optional) Override value for the RPC layer used by
          TensorFlow.
        task_type - (Optional) Override value for the current task type.
        task_id - (Optional) Override value for the current task index.

    Raises:
      TypeError: If any argument is not a subclass of `ClusterResolvers`.
      ValueError: If there are no arguments passed.
    """
super(UnionClusterResolver, self).__init__()

self._rpc_layer = kwargs.pop('rpc_layer', None)
self._task_type = kwargs.pop('task_type', None)
self._task_id = kwargs.pop('task_id', None)

if kwargs:
    raise ValueError('Unexpected kwargs provided {!r}'.format(kwargs))

if not args:
    raise ValueError('At least one ClusterResolver is required.')

for cluster_resolver in args:
    if not isinstance(cluster_resolver, ClusterResolver):
        raise TypeError('All arguments must be a sub-class of '
                        '`ClusterResolver.`')
self._cluster_resolvers = args
