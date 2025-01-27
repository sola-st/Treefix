# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Returns the master address to use when creating a session.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (Optional) The type of the TensorFlow task of the master.
      task_id: (Optional) The index of the TensorFlow task of the master.
      rpc_layer: (Optional) The RPC used by distributed TensorFlow.

    Returns:
      The name or URL of the session master.

    If a task_type and task_id is given, this will override the `master`
    string passed into the initialization function.
    """
if task_type is not None and task_id is not None:
    master = self.cluster_spec().task_address(task_type, task_id)
else:
    master = self._master

exit(format_master_url(master, rpc_layer=rpc_layer or self._rpc_layer))
