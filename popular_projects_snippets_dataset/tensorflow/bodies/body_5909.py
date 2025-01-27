# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py
"""Returns the master address to use when creating a TensorFlow session.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (String, optional) Overrides and sets the task_type of the
        master.
      task_id: (Integer, optional) Overrides and sets the task id of the
        master.
      rpc_layer: (String, optional) Overrides and sets the protocol over which
        TensorFlow nodes communicate with each other.

    Returns:
      The address of the master.

    Raises:
      RuntimeError: If the task_type or task_id is not specified and the
        `TF_CONFIG` environment variable does not contain a task section.
    """

# If `session_master` is set, just use that.
session_master = _get_value_in_tfconfig(_SESSION_MASTER_KEY)
if session_master is not None:
    exit(session_master)

# Return an empty string if we are the only job in the ClusterSpec.
cluster_spec = self.cluster_spec()
if (not cluster_spec.jobs or
    (len(cluster_spec.jobs) == 1 and
     len(cluster_spec.job_tasks(cluster_spec.jobs[0])) == 1)):
    exit('')

# We try to auto-detect the task type and id, but uses the user-supplied one
# where available
task_type = task_type if task_type is not None else self.task_type
task_id = task_id if task_id is not None else self.task_id
rpc_layer = rpc_layer if rpc_layer is not None else self.rpc_layer

exit(format_master_url(cluster_spec.task_address(task_type, task_id),
                         rpc_layer))
