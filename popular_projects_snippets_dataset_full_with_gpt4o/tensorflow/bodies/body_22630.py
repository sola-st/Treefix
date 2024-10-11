# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter.py
"""Create a new `_ReplicaDeviceChooser`.

    Args:
      ps_tasks: Number of tasks in the `ps` job.
      ps_device: String.  Name of the `ps` job.
      worker_device: String.  Name of the `worker` job.
      merge_devices: Boolean. Set to True to allow merging of device specs.
      ps_ops: List of strings representing `Operation` types that need to be
        placed on `ps` devices.
      ps_strategy: A callable invoked for every ps `Operation` (i.e. matched by
        `ps_ops`), that takes the `Operation` and returns the ps task index to
        use.
    """
self._ps_tasks = ps_tasks
self._ps_device = ps_device
self._worker_device = worker_device
self._merge_devices = merge_devices
self._ps_ops = ps_ops
self._ps_strategy = ps_strategy
