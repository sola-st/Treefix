# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Initializes the object.

    Args:
      devices: a list of device strings to run collectives on.
      group_size: the global group size. For between-graph replicated training
        it's the total number of devices across all workers.
      options: a `tf.distribute.experimental.CommunicationOptions`.
      collective_keys: an optional CollectiveKey object.
      canonicalize_devices: Whether to canonicalize devices for workers or not.
    """
if group_size % len(devices) > 0:
    raise ValueError("group_size must be divisible by the number of devices.")

self._group_size = group_size
self._options = options
self._collective_keys = (collective_keys or
                         cross_device_utils.CollectiveKeys())
# This lock guards all collective launches, i.e. calls to
# cross_device_utils.build_collectve_*.
#
# In a multi threaded eager program we need to ensure different groups of
# collectives don't interleave each other, otherwise there could be
# deadlocks. E.g. if two user threads both are launching collectives:
#   user-thread-0  device0                 device1
#   user-thread-1          device0 device1
# In eager mode, we use one thread per device to launch collective ops, so
# the above launch sequences end up with the following queues:
#   device-0  collective-0  collective-1
#   device-1  collective-1  collective-0
# This deadlocks since neither collective is able to finish.
self._lock = threading.Lock()

if canonicalize_devices:
    self._devices = tuple(device_util.canonicalize(d) for d in devices)
else:
    self._devices = tuple(
        device_util.canonicalize_without_job_and_task(d) for d in devices)
group_key = self._collective_keys.get_group_key(self._devices)
self._launchers = []
# Whether to only use NCCL for batched all-reduce when NCCL is requested.
# This is because of the lack of mechanism to order NCCL operations
# deterministically.
self._limited_nccl = False
for device in self._devices:
    launcher = cross_device_utils.CollectiveReplicaLauncher(
        group_key, group_size, self._collective_keys, device, options)
    self._launchers.append(launcher)
    if not launcher.can_order_nccl():
        self._limited_nccl = True

super(CollectiveAllReduce, self).__init__()
self._canonicalize_devices = canonicalize_devices
