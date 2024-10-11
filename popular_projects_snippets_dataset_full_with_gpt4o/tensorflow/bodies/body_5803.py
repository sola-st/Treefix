# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Get the Master string to be used for the session.

    In the normal case, this returns the grpc path (grpc://1.2.3.4:8470) of
    first instance in the ClusterSpec returned by the cluster_spec function.

    If a non-TPU name is used when constructing a TPUClusterResolver, that will
    be returned instead (e.g. If the tpus argument's value when constructing
    this TPUClusterResolver was 'grpc://10.240.1.2:8470',
    'grpc://10.240.1.2:8470' will be returned).

    Args:
      task_type: (Optional, string) The type of the TensorFlow task of the
        master.
      task_id: (Optional, integer) The index of the TensorFlow task of the
        master.
      rpc_layer: (Optional, string) The RPC protocol TensorFlow should use to
        communicate with TPUs.

    Returns:
      string, the connection string to use when creating a session.

    Raises:
      ValueError: If none of the TPUs specified exists.
    """

if self._tpu != 'local':
    cluster_spec = self.cluster_spec()
    if task_type is not None and task_id is not None:
        # task_type and task_id is from the function parameter
        master = cluster_spec.task_address(task_type, task_id)
    elif self.task_type is not None and self.task_id is not None:
        # task_type and task_id is from the object
        master = cluster_spec.task_address(self.task_type, self.task_id)
    else:
        # by default we take the first item in the cluster with the right name
        job_tasks = cluster_spec.job_tasks(self.task_type)
        if not job_tasks:
            raise ValueError('No TPUs with the specified names exist.')
        master = job_tasks[0]
    exit(cluster_resolver.format_master_url(master, 'grpc'))
else:
    exit('')
