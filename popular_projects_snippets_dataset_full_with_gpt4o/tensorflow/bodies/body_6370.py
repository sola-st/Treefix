# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Initializes the object for multi-worker training."""
cluster_spec = multi_worker_util.normalize_cluster_spec(
    cluster_resolver.cluster_spec())
task_type = cluster_resolver.task_type
task_id = cluster_resolver.task_id
if task_type is None or task_id is None:
    raise ValueError("When `cluster_spec` is given, you must also specify "
                     "`task_type` and `task_id`.")
self._cluster_spec = cluster_spec
self._task_type = task_type
self._task_id = task_id
self._id_in_cluster = multi_worker_util.id_in_cluster(
    self._cluster_spec, self._task_type, self._task_id)

self._num_workers = multi_worker_util.worker_count(cluster_spec, task_type)
if not self._num_workers:
    raise ValueError("No `worker`, `chief` or `evaluator` tasks can be found "
                     "in `cluster_spec`.")

self._is_chief = multi_worker_util.is_chief(cluster_spec, task_type,
                                            task_id)

self._worker_device = "/job:%s/task:%d" % (task_type, task_id)
self._host_input_device = numpy_dataset.SingleDevice(self._worker_device)

if (ops.executing_eagerly_outside_functions() and
    not getattr(self, "_local_or_standalone_client_mode", False)):
    context.context().configure_collective_ops(
        collective_leader=multi_worker_util.collective_leader(
            cluster_spec, task_type, task_id),
        scoped_allocator_enabled_ops=("CollectiveReduce",),
        device_filters=("/job:%s/task:%d" % (task_type, task_id),))
    self._collective_ops_configured = True
    if context.context().coordination_service is None:
        coordinated_jobs = ["chief", "worker"]
        if task_type in coordinated_jobs:
            coordinated_job_config = []
            for job in coordinated_jobs:
                if job in cluster_spec.jobs:
                    coordinated_job_config.append(
                        coordination_config_pb2.CoordinatedJob(
                            name=job,
                            num_tasks=cluster_spec.num_tasks(job)))
            context.context().configure_coordination_service(
                service_type="standalone",
                service_leader=multi_worker_util.coordination_leader(
                    cluster_spec),
                coordinated_jobs=coordinated_job_config)

    # Starting a std server in eager mode and in independent worker mode.
if (context.executing_eagerly() and
    not getattr(self, "_std_server_started", False) and
    not getattr(self, "_local_or_standalone_client_mode", False)):
    # Checking _local_or_standalone_client_mode as well because we should not
    # create the std server in standalone client mode.
    config_proto = copy.deepcopy(context.context().config)
    config_proto = self._update_config_proto(config_proto)

    # If coordination service is enabled, use its internal heartbeat to detect
    # peer failures instead of the Python-level health check.
    if config_proto.experimental.coordination_config.service_type:
        self._enable_check_health = False

    if hasattr(cluster_resolver, "port"):
        port = cluster_resolver.port
    else:
        port = 0
    server_def = tensorflow_server_pb2.ServerDef(
        cluster=cluster_spec.as_cluster_def(),
        default_session_config=config_proto,
        job_name=task_type,
        task_index=task_id,
        protocol=cluster_resolver.rpc_layer or "grpc",
        port=port)
    context.context().enable_collective_ops(server_def)
    self._std_server_started = True
    # The `ensure_initialized` is needed before calling
    # `context.context().devices()`.
    context.context().ensure_initialized()
    logging.info(
        "Enabled multi-worker collective ops with available devices: %r",
        context.context().devices())

# TODO(yuefengz): The `num_gpus` is only for this particular task. It
# assumes all workers have the same number of GPUs. We should remove this
# assumption by querying all tasks for their numbers of GPUs.
# TODO(b/126786766): TFConfigClusterResolver returns wrong number of GPUs in
# some cases.
local_devices, local_device_type = self._initialize_local_devices(
    cluster_resolver, self._worker_device)
if local_device_type == "TPU":
    tpu_strategy_util.initialize_tpu_system()

self._collective_keys = cross_device_utils.CollectiveKeys(
    group_key_start=1 + self._collective_key_base)
self._cross_device_ops = cross_device_ops_lib.CollectiveAllReduce(
    devices=local_devices,
    group_size=len(local_devices) * self._num_workers,
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

# Add a default device so that ops without specified devices will not end up
# on other workers.
self._default_device = "/job:%s/task:%d" % (task_type, task_id)

# Save the num_devices_per_worker and rpc_layer for configure method.
self._num_devices_per_worker = len(local_devices)
self._local_device_type = local_device_type
self._rpc_layer = cluster_resolver.rpc_layer
self._warn_nccl_no_gpu()

if self._enable_check_health and context.executing_eagerly():
    self._start_check_health_thread()
else:
    logging.info("Check health not enabled.")

logging.info(
    "MultiWorkerMirroredStrategy with cluster_spec = %r, task_type = %r, "
    "task_id = %r, num_workers = %r, local_devices = %r, "
    "communication = %s", cluster_spec.as_dict(), task_type, task_id,
    self._num_workers, local_devices,
    self._communication_options.implementation)
