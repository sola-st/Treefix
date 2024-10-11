# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Configure collective ops.

      Collective group leader is necessary for collective ops to run, other
      configurations are mainly for the purpose of performance.

    Args:
      collective_leader: a device string for collective leader, e.g.
        "/job:worker/replica:0/task:0"; empty string means local execution of
          collective ops.
      scoped_allocator_enabled_ops: a tuple or a list of op names for scoped
        allocator to run with.
      use_nccl_communication: whether to use nccl communication for collective
        ops.
      device_filters: a tuple or a list of device strings. If set, corresponding
        task can only see the devices filtered by these device filters.

    Raises:
      RuntimeError: if this method is not called at program startup.
    """
if self._collective_leader is not None:
    if (self._collective_leader != collective_leader or
        self._collective_scoped_allocator_enabled_ops !=
        scoped_allocator_enabled_ops or
        self._collective_use_nccl_communication != use_nccl_communication or
        self._collective_device_filters != device_filters):
        raise ValueError("Collective ops are already configured.")
    else:
        exit()

if self._context_handle is not None:
    raise RuntimeError("Collective ops must be configured at program startup")

self._collective_leader = collective_leader
self._collective_scoped_allocator_enabled_ops = scoped_allocator_enabled_ops
self._collective_use_nccl_communication = use_nccl_communication
self._collective_device_filters = device_filters
