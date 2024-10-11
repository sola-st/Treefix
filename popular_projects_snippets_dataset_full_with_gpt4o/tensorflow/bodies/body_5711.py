# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Returns the number of accelerator cores per worker.

    This returns the number of accelerator cores (such as GPUs and TPUs)
    available per worker.

    Optionally, we allow callers to specify the task_type, and task_id, for
    if they want to target a specific TensorFlow task to query
    the number of accelerators. This is to support heterogenous environments,
    where the number of accelerators cores per host is different.

    Args:
      task_type: (Optional) The type of the TensorFlow task of the machine we
        want to query.
      task_id: (Optional) The index of the TensorFlow task of the machine we
        want to query.
      config_proto: (Optional) Configuration for starting a new session to
        query how many accelerator cores it has.

    Returns:
      A map of accelerator types to number of cores.
    """
master = self.master(task_type, task_id)
# TODO(b/126786766): in eager mode, we should check whether
# `tf.config.experimental_connect_to_cluster` is called or not.
devices = get_accelerator_devices(master, config_proto)
mapping = collections.defaultdict(int)
for device in devices:
    if task_type is not None and task_id is not None:
        job_path = '/job:%s' % task_type
        task_path = '/task:%s' % task_id
        if job_path not in device.name or task_path not in device.name:
            continue
    mapping[device.device_type] += 1
exit(mapping)
