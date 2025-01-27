# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Initializes the object for local training."""
self._is_chief = True
self._num_workers = 1

if ops.executing_eagerly_outside_functions():
    try:
        context.context().configure_collective_ops(
            scoped_allocator_enabled_ops=("CollectiveReduce",))
    except RuntimeError:
        logging.warning("Collective ops is not configured at program startup. "
                        "Some performance features may not be enabled.")
    self._collective_ops_configured = True

if devices:
    local_devices = devices
    if "GPU" in devices[0]:
        local_device_type = "GPU"
    elif "TPU" in devices[0]:
        local_device_type = "TPU"
    else:
        local_device_type = "CPU"
else:
    local_devices, local_device_type = self._initialize_local_devices(
        cluster_resolver, worker_device="")

self._worker_device = device_util.canonicalize("/device:CPU:0")
self._host_input_device = numpy_dataset.SingleDevice(self._worker_device)

self._collective_keys = cross_device_utils.CollectiveKeys(
    group_key_start=1 + self._collective_key_base)
self._cross_device_ops = cross_device_ops_lib.CollectiveAllReduce(
    devices=local_devices,
    group_size=len(local_devices),
    options=self._communication_options,
    collective_keys=self._collective_keys)
# CrossDeviceOps for per host tensors.
self._host_cross_device_ops = cross_device_ops_lib.CollectiveAllReduce(
    devices=[self._worker_device],
    group_size=self._num_workers,
    options=self._communication_options,
    collective_keys=self._collective_keys)
super(CollectiveAllReduceExtended, self)._initialize_single_worker(
    local_devices)

self._cluster_spec = None
self._task_type = None
self._task_id = None
self._id_in_cluster = 0

# This is a mark to tell whether we are running with standalone client or
# independent worker. Right now with standalone client, strategy object is
# created as local strategy and then turn into multi-worker strategy via
# configure call.
self._local_or_standalone_client_mode = True

# Save the num_devices_per_worker and rpc_layer for configure method.
self._num_devices_per_worker = len(local_devices)
self._local_device_type = local_device_type
self._rpc_layer = cluster_resolver.rpc_layer
self._warn_nccl_no_gpu()

logging.info(
    "Single-worker MultiWorkerMirroredStrategy with local_devices "
    "= %r, communication = %s", local_devices,
    self._communication_options.implementation)
