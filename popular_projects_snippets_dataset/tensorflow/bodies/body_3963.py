# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/accelerator_util.py
"""Initializes accelerators and communication fabrics for DTensor.

  DTensor configures TensorFlow to run in the local mode or multi-client mode.
  - In local mode, a mesh can only use devices attached to the current process.
  - In multi-client mode, a mesh can span across devices from multiple clients.

  If `DTENSOR_JOBS` is non-empty, DTensor configures TensorFlow to run in the
  multi-client mode using the distributed runtime. In multi-client mode devices
  on different clients can communicate with each other.

  The following environment variables controls the behavior of this function.

  - `DTENSOR_JOBS`: string, a comma separated list. Each item in the list is
      of format `{hostname}:{port}`. If empty, DTensor runs in the local mode.
      Examples of valid `DTENSOR_JOBS` values:
      - 4 clients on localhost:
        `localhost:10000,localhost:10001,localhost:10002,localhost:10003`
      - 2 clients on host1, 2 clients on host2
        `host1:10000,host1:10001,host2:10000,host2:10003`
      If the hostnames are BNS addresses, the items must be sorted in
      alphabetical order.
  - `DTENSOR_CLIENT_ID`: integer, between `0` to `num_clients - 1`, to identify
      the client id of the current process. The default value is `0`.
  - `DTENSOR_JOB_NAME`: string, a string for the name of the TensorFlow job.
      The job name controls the job name section of the TensorFlow DeviceSpecs,
      e.g., `job:worker` in `/job:worker/replica:0/task:0/device:TPU:0` when
      the job name is `worker`.
      The default value is `localhost` in local mode, and
      `worker` when in the multi-client mode. All DTensor clients within the
      same multi-client cluster share the same job name.
  - `DTENSOR_USE_PARALLEL_EXECUTOR`: string, with its value being `pw` to
      specify that the backend is Pathways, and TensorFlow otherwise.

  Args:
    device_type: Type of accelerator to use, can be CPU, GPU, or TPU. If None,
      uses `tf.experimental.dtensor.preferred_device_type()`.
    enable_coordination_service: If true, enable distributed coordination
      service to make sure that workers know the devices on each other, when
      there is more than 1 client.

  Returns:
    device_type: the type of accelerator that was initialized.
  """
global _INITIALIZED_ACCELERATOR_SYSTEM_TYPE
assert context.executing_eagerly()

if is_initialized():
    raise ValueError(
        "Accelerator system has already been initialized. "
        "Call tf.experimental.dtensor.shutdown_accelerator_system() first.")

if context.context()._initialized:  # pylint: disable=protected-access
    raise ValueError(
        "TensorFlow has already been initialized. "
        "tf.experimental.dtensor.initialize_accelerator_system() must be "
        "called before TensorFlow is initialized.")

context.context()._clear_caches()  # pylint: disable=protected-access

if device_type is None:
    device_type = config.preferred_device_type()

device_type = device_type.upper()
if device_type not in {"CPU", "GPU", "TPU"}:
    raise ValueError(f"Unknown device_type {device_type}. "
                     "Allowed values are CPU, GPU, or TPU")

if config.gpu_use_nccl_communication():
    logical_gpu_count = config.num_local_devices("GPU")
    physical_gpu_count = len(tf_config.list_physical_devices("GPU"))
    if logical_gpu_count != physical_gpu_count:
        raise ValueError(
            f"DTENSOR_GPU_USE_NCCL_COMMUNICATION is set for using NCCL. "
            f"NCCL Collectives require same number of logical and physical GPUs. "
            f"The number of logical GPU ({logical_gpu_count}) "
            f"differs from the number of physical GPU ({physical_gpu_count}).")

  # Configure logical host CPU devices for accelerators.
if device_type in ("GPU", "TPU"):
    num_local_devices = config.num_local_devices(device_type)
    if config.num_local_devices("CPU") < num_local_devices:
        tf_config.set_logical_device_configuration(
            tf_config.list_physical_devices("CPU")[0],
            [context.LogicalDeviceConfiguration()] * num_local_devices)

if not config.is_local_mode():
    initialize_multi_client_cluster(
        job_name=config.job_name(),
        dtensor_jobs=config.jobs(),
        client_id=config.client_id(),
        collective_leader=config.full_job_name(task_id=0),
        gpu_use_nccl_communication=config.gpu_use_nccl_communication(),
        enable_coordination_service=enable_coordination_service)
else:
    if device_type == "GPU":
        # Enables Nccl on local mode.
        context.context(  # pylint: disable=protected-access
        )._collective_use_nccl_communication = config.gpu_use_nccl_communication(
        )

if device_type == "TPU" and not config.backend_is_pw():
    tpu_util.initialize_tpu_system()

_INITIALIZED_ACCELERATOR_SYSTEM_TYPE = device_type

exit(device_type)
