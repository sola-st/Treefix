# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
super(TPUExtended, self).__init__(container_strategy)

if tpu_cluster_resolver is None:
    tpu_cluster_resolver = TPUClusterResolver("")

if steps_per_run is None:
    # TODO(frankchn): Warn when we are being used by DS/Keras and this is
    # not specified.
    steps_per_run = 1

# `self._tpu_function_cache` is a dict of `tf.function`s, thus if a
# `tf.function` is passed into `strategy.run` in eager mode, the
# `tf.function` won't get retraced.
self._tpu_function_cache = weakref.WeakKeyDictionary()

self._tpu_cluster_resolver = tpu_cluster_resolver
self._tpu_metadata = self._tpu_cluster_resolver.get_tpu_system_metadata()
self._device_assignment = device_assignment

tpu_devices_flat = [
    d.name for d in self._tpu_metadata.devices if "device:TPU:" in d.name]

# `self._tpu_devices` is a two-dimensional NumPy array of strings. It is
# indexed using `[replica_id][logical_device_id]`.
if device_assignment is None:
    self._tpu_devices = np.array(
        [[d] for d in tpu_devices_flat], dtype=object)
else:
    job_name = device_spec.DeviceSpecV2.from_string(tpu_devices_flat[0]).job

    tpu_devices = []
    for replica_id in range(device_assignment.num_replicas):
        replica_devices = []

        for logical_core in range(device_assignment.num_cores_per_replica):
            replica_devices.append(
                device_util.canonicalize(
                    device_assignment.tpu_device(
                        replica=replica_id,
                        logical_core=logical_core,
                        job=job_name)))

        tpu_devices.append(replica_devices)
    self._tpu_devices = np.array(tpu_devices, dtype=object)

self._host_device = device_util.get_host_for_device(self._tpu_devices[0][0])

# Preload the data onto the TPUs. Currently we always preload onto logical
# device 0 for each replica.
# TODO(cjfj): Create `InputWorkers` lazily, allowing users to place the
# input onto a different logical device?
self._device_input_worker_devices = collections.OrderedDict()
self._host_input_worker_devices = collections.OrderedDict()
for tpu_device in self._tpu_devices[:, 0]:
    host_device = device_util.get_host_for_device(tpu_device)
    self._device_input_worker_devices.setdefault(host_device, [])
    self._device_input_worker_devices[host_device].append(tpu_device)
    self._host_input_worker_devices.setdefault(host_device, [])
    self._host_input_worker_devices[host_device].append(host_device)

# TODO(sourabhbajaj): Remove this once performance of running one step
# at a time is comparable to multiple steps.
self.steps_per_run = steps_per_run
self._require_static_shapes = True

self.experimental_enable_get_next_as_optional = True

self._logical_device_stack = [0]

if context.executing_eagerly():
    # In async remote eager, we want to sync the executors before exiting the
    # program.
    atexit.register(context.async_wait)

# Flag to turn on VariablePolicy. Var policy is deprecated because there is
# another effort unifying DistributedVariables (see values_v2.py). SPMD XLA
# partitioning is not implemented for var policies.
# TODO(b/202048882): remove var policy from TPUStrategy.
self._use_var_policy = not use_spmd_for_xla_partitioning

# Flag to enable XLA SPMD partitioning.
self._use_spmd_for_xla_partitioning = use_spmd_for_xla_partitioning
