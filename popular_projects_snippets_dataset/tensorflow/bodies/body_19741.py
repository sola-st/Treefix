# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_strategy_util.py
"""Initialize the TPU devices.

  Args:
    cluster_resolver: A tf.distribute.cluster_resolver.TPUClusterResolver,
        which provides information about the TPU cluster.
  Returns:
    The tf.tpu.Topology object for the topology of the TPU cluster. If called
    inside tf.function, it returns the serialized topology object instead.

  Raises:
    RuntimeError: If running inside a tf.function.
    NotFoundError: If no TPU devices found in eager mode.
  """

# Deallocate all TPU buffers by clearing out eager context caches and
# triggering garbage collection to avoid keeping invalid tpu buffer around
# after reinitialized tpu system.
logging.info("Deallocate tpu buffers before initializing tpu system.")
context.context()._clear_caches()  # pylint: disable=protected-access
context.context().clear_kernel_cache()
gc.collect()

job = None
if cluster_resolver is None:
    # If no cluster resolver is specified, and running eagerly, execute the init
    # ops in the current device scope.
    if context.executing_eagerly():
        curr_device = device.DeviceSpec.from_string(context.context().device_name)
        if curr_device.job is not None:
            job = "{}/replica:0/task:0".format(curr_device.job)

    cluster_resolver = TPUClusterResolver("")
assert isinstance(cluster_resolver, TPUClusterResolver)

tpu_name = compat.as_text(cluster_resolver._tpu)  # pylint: disable=protected-access
if tpu_name in _INITIALIZED_TPU_SYSTEMS:
    logging.warning(
        "TPU system %s has already been initialized. "
        "Reinitializing the TPU can cause previously created "
        "variables on TPU to be lost.", tpu_name)

logging.info("Initializing the TPU system: %s", tpu_name)

# This function looks as it is for the following non-intuitive reasons.
# tpu.initialize_system creates a dummy op whose sole purpose is to trigger
# DistributedTPURewritePass. This pass actually adds real ops that
# initialize the TPU system. Thus, we can't simply run tpu.initialize_system
# eagerly. We need to wrap it in defun and trigger the rewrite passes on it.
if tpu_name not in _LOCAL_MASTERS:
    # Explicitly place the tpu.initialize_system in the first worker to
    # avoid the output node match multiple devices error.
    job = "{}/replica:0/task:0".format(cluster_resolver.get_job_name())

if context.executing_eagerly():
    @function
    def _tpu_init_fn():
        # In TF1, we usually close chips when compilation fails to clear the data
        # in infeed. In TF2, we don't need to do this because infeed is no longer
        # used, so user can recover from TPU compilation failures more smoothly.
        # Same for the cancellation of a TPU excution.
        exit(tpu.initialize_system(
            job=job,
            compilation_failure_closes_chips=False,
            tpu_cancellation_closes_chips=False))

    # The TPU_SYSTEM device must match the device used in tpu.initialize_system
    # exactly, otherwise you can get errors if there are multiple TPU_SYSTEM
    # devices available.
    try:
        with ops.device(tpu._tpu_system_device_name(job)):  # pylint: disable=protected-access
            output = _tpu_init_fn()
        context.async_wait()
    except errors.InvalidArgumentError as e:
        raise errors.NotFoundError(
            None, None,
            "TPUs not found in the cluster. Failed in initialization: "
            + str(e))

    # Clear out the eager context caches since the memory is invalid now.
    context.context()._initialize_logical_devices()  # pylint: disable=protected-access

    serialized_topology = output.numpy()
elif not ops.executing_eagerly_outside_functions():
    master = cluster_resolver.master()
    cluster_spec = cluster_resolver.cluster_spec()

    session_config = config_pb2.ConfigProto(allow_soft_placement=True)
    if cluster_spec:
        session_config.cluster_def.CopyFrom(cluster_spec.as_cluster_def())

    with ops.Graph().as_default():
        with session_lib.Session(config=session_config, target=master) as sess:
            serialized_topology = sess.run(tpu.initialize_system())
else:
    with ops.device(tpu._tpu_system_device_name(job)):  # pylint: disable=protected-access
        serialized_topology = tpu.initialize_system(
            job=job, compilation_failure_closes_chips=False)
        # If initialize_tpu_system is called inside tf.function, we only return
        # the serialized topology object as the tf.tpu.Topology object has to be
        # constructed in eager mode.
        exit(serialized_topology)

logging.info("Finished initializing TPU system.")
tpu_topology = topology.Topology(serialized=serialized_topology)
cluster_resolver.set_tpu_topology(serialized_topology)
_INITIALIZED_TPU_SYSTEMS[tpu_name] = tpu_topology

# Record the address of the TPU worker-0 that the coordinator connects to.
# This can be used to associate the TPU worker with the right coordinator when
# aggregating the metrics for the application. An example of the address:
# /bns/mb/borg/mb/bns/chienchunh/chienchunh_group_49640234.1.tfm_train_tpu_worker/0
_tpu_worker_address.get_cell("address").set(cluster_resolver.get_master())

exit(tpu_topology)
