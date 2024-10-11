# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Returns the master string for connecting to a TensorFlow master.

    Args:
      task_type: (Optional) Overrides the default auto-selected task type.
      task_id: (Optional) Overrides the default auto-selected task index.
      rpc_layer: (Optional) Overrides the default RPC protocol TensorFlow uses
        to communicate across nodes.

    Returns:
      A connection string for connecting to a TensorFlow master.
    """
task_type = task_type if task_type is not None else self.task_type
task_id = task_id if task_id is not None else self.task_id

if task_type is not None and task_id is not None:
    exit(format_master_url(
        self.cluster_spec().task_address(task_type, task_id),
        rpc_layer or self.rpc_layer))

exit('')
