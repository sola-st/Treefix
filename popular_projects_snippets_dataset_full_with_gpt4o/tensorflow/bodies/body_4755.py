# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
"""Initialize local devices for training."""
self._worker_device = device_util.canonicalize("/device:CPU:0")
self._input_host_device = numpy_dataset.SingleDevice(self._worker_device)

if compute_devices is None:
    if not cluster_resolver:
        num_gpus = context.num_gpus()
    else:
        num_gpus = cluster_resolver.num_accelerators().get("GPU", 0)
    # Save the num_gpus_per_worker for configure method which is used by the
    # contrib version.
    self._num_gpus_per_worker = num_gpus

    compute_devices = device_util.local_devices_from_num_gpus(num_gpus)

compute_devices = [device_util.canonicalize(d) for d in compute_devices]

if parameter_device is None:
    # If there is only one GPU, put everything on that GPU. Otherwise, place
    # variables on CPU.
    if len(compute_devices) == 1:
        parameter_device = compute_devices[0]
    else:
        parameter_device = _LOCAL_CPU

self._variable_device = parameter_device
self._compute_devices = compute_devices
self._parameter_devices = (parameter_device,)
self._is_chief = True
self._cluster_spec = None
self._task_type = None
self._task_id = None

logging.info(
    "ParameterServerStrategy (CentralStorageStrategy if you are using a "
    "single machine) with compute_devices = %r, variable_device = %r",
    compute_devices, self._variable_device)
