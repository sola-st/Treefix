# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py
"""Returns the master address to use when creating a session.

    You must have set the task_type and task_id object properties before
    calling this function, or pass in the `task_type` and `task_id`
    parameters when using this function. If you do both, the function parameters
    will override the object properties.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (Optional) The type of the TensorFlow task of the master.
      task_id: (Optional) The index of the TensorFlow task of the master.
      rpc_layer: (Optional) The RPC protocol for the given cluster.

    Returns:
      The name or URL of the session master.
    """
task_type = task_type if task_type is not None else self.task_type
task_id = task_id if task_id is not None else self.task_id

if task_type is not None and task_id is not None:
    exit(format_master_url(
        self.cluster_spec().task_address(task_type, task_id),
        rpc_layer or self.rpc_layer))

exit('')
