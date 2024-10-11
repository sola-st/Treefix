# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Initializes the object for multi-worker training."""
device_dict = _group_device_list(devices)
workers = []
worker_devices = []
for job in ("chief", "worker"):
    for task in range(len(device_dict.get(job, []))):
        worker = "/job:%s/task:%d" % (job, task)
        workers.append(worker)
        worker_devices.append((worker, device_dict[job][task]))

    # Setting `_default_device` will add a device scope in the
    # distribution.scope. We set the default device to the first worker. When
    # users specify device under distribution.scope by
    #   with tf.device("/cpu:0"):
    #     ...
    # their ops will end up on the cpu device of its first worker, e.g.
    # "/job:worker/task:0/device:CPU:0". Note this is not used in replica mode.
self._default_device = workers[0]
self._host_input_device = numpy_dataset.SingleDevice(workers[0])

self._devices = tuple(devices)
self._input_workers_devices = worker_devices
self._is_multi_worker_training = True

if len(workers) > 1:
    # Grandfather usage in the legacy tests if they're configured properly.
    if (not isinstance(self._cross_device_ops,
                       cross_device_ops_lib.ReductionToOneDevice) or
        self._cross_device_ops._num_between_graph_workers > 1):  # pylint: disable=protected-access
        raise ValueError(
            "In-graph multi-worker training with `MirroredStrategy` is not "
            "supported.")
    self._inferred_cross_device_ops = self._cross_device_ops
else:
    # TODO(yuefengz): make `select_cross_device_ops` work with device strings
    # containing job names.
    self._inferred_cross_device_ops = cross_device_ops_lib.NcclAllReduce()

logging.info("Using MirroredStrategy with remote devices %r", devices)
