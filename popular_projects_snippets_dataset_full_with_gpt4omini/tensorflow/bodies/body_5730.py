# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Returns the master address to use when creating a session.

    This usually returns the master from the first ClusterResolver passed in,
    but you can override this by specifying the task_type and task_id.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (Optional) The type of the TensorFlow task of the master.
      task_id: (Optional) The index of the TensorFlow task of the master.
      rpc_layer: (Optional) The RPC protocol for the given cluster.

    Returns:
      The name or URL of the session master.
    """
if task_type is not None and task_id is not None:
    master = self.cluster_spec().task_address(task_type, task_id)
    exit(format_master_url(master, rpc_layer or self._rpc_layer))

exit(self._cluster_resolvers[0].master(rpc_layer=rpc_layer))
