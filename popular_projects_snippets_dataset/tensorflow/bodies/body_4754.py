# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
"""Initialize devices for multiple workers.

    It creates variable devices and compute devices. Variables and operations
    will be assigned to them respectively. We have one compute device per
    replica. The variable device is a device function or device string. The
    default variable device assigns variables to parameter servers in a
    round-robin fashion.

    Args:
      cluster_resolver: a descendant of `ClusterResolver` object.

    Raises:
      ValueError: if the cluster doesn't have ps jobs.
    """
# TODO(b/126786766): TFConfigClusterResolver returns wrong number of GPUs in
# some cases.
if isinstance(cluster_resolver, TFConfigClusterResolver):
    num_gpus = context.num_gpus()
else:
    num_gpus = cluster_resolver.num_accelerators().get("GPU", 0)

# Save the num_gpus_per_worker for configure method.
self._num_gpus_per_worker = num_gpus

cluster_spec = cluster_resolver.cluster_spec()
task_type = cluster_resolver.task_type
task_id = cluster_resolver.task_id
if not task_type or task_id is None:
    raise ValueError("When `cluster_spec` is given, you must also specify "
                     "`task_type` and `task_id`")
cluster_spec = multi_worker_util.normalize_cluster_spec(cluster_spec)
assert cluster_spec.as_dict()

self._worker_device = "/job:%s/task:%d" % (task_type, task_id)
self._input_host_device = numpy_dataset.SingleDevice(self._worker_device)

# Define compute devices which is a list of device strings and one for each
# replica. When there are GPUs, replicate operations on these GPUs.
# Otherwise, place operations on CPU.
if num_gpus > 0:
    compute_devices = tuple(
        "%s/device:GPU:%d" % (self._worker_device, i)
        for i in range(num_gpus))
else:
    compute_devices = (self._worker_device,)

self._compute_devices = [
    device_util.canonicalize(d) for d in compute_devices]

# In distributed mode, place variables on ps jobs in a round-robin fashion.
# Note that devices returned from `replica_device_setter` are not
# canonical and therefore we don't canonicalize all variable devices to
# make them consistent.
# TODO(yuefengz): support passing a strategy object to control variable
# assignment.
# TODO(yuefengz): merge the logic of replica_device_setter into this
# class.
num_ps_replicas = len(cluster_spec.as_dict().get("ps", []))
if num_ps_replicas == 0:
    raise ValueError("The cluster spec needs to have `ps` jobs.")
self._variable_device = device_setter.replica_device_setter(
    ps_tasks=num_ps_replicas,
    worker_device=self._worker_device,
    merge_devices=True,
    cluster=cluster_spec)

# The `_parameter_devices` is needed for the `parameter_devices` property
# and is a list of all variable devices. Here parameter devices are all
# tasks of the "ps" job.
self._parameter_devices = tuple(map("/job:ps/task:{}".format,
                                    range(num_ps_replicas)))

# Add a default device so that ops without specified devices will not end up
# on other workers.
self._default_device = self._worker_device

self._is_chief = multi_worker_util.is_chief(cluster_spec, task_type,
                                            task_id)
self._cluster_spec = cluster_spec
self._task_type = task_type
self._task_id = task_id

logging.info(
    "Multi-worker ParameterServerStrategy with "
    "cluster_spec = %r, task_type = %r, task_id = %r, "
    "num_ps_replicas = %r, is_chief = %r, compute_devices = %r, "
    "variable_device = %r", cluster_spec.as_dict(), task_type, task_id,
    num_ps_replicas, self._is_chief, self._compute_devices,
    self._variable_device)
