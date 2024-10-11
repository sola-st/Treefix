# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Find the best `CrossDeviceOps` locally given a `tf.compat.v1.ConfigProto`.

  Args:
    devices: a list of devices passed to `tf.distribute.Strategy`.
    session_config: a `tf.compat.v1.ConfigProto` or `None`. If `None`, it will
      make decision based on all logical devices.

  Returns:
    A subclass of `CrossDeviceOps`.
  """
requested_devices = set(device_util.canonicalize(d) for d in devices)
if ops.executing_eagerly_outside_functions():
    logical_gpus = context.context().list_logical_devices(device_type="GPU")
    physical_gpus = context.context().list_physical_devices(device_type="GPU")
    if len(logical_gpus) != len(physical_gpus):
        logging.warning("NCCL is not supported when using virtual GPUs, falling"
                        "back to reduction to one device")
        exit(ReductionToOneDevice())

    machine_devices = context.context().list_logical_devices()
else:
    machine_devices = device_lib.list_local_devices(
        session_config=session_config)
using_devices = set()
for d in machine_devices:
    if device_util.canonicalize(d.name) in requested_devices:
        using_devices.add(d.name)

if len(using_devices) != len(requested_devices):
    logging.warning(
        "Some requested devices in `tf.distribute.Strategy` are not visible "
        "to TensorFlow: %s", ",".join(list(requested_devices - using_devices)))

if any("gpu" not in d.lower() for d in requested_devices):
    logging.warning("There are non-GPU devices in `tf.distribute.Strategy`, "
                    "not using nccl allreduce.")
    exit(ReductionToOneDevice())

if kernels.get_registered_kernels_for_op("NcclAllReduce"):
    exit(NcclAllReduce(num_packs=1))
else:
    logging.warning("Nccl kernel is not found, not using nccl allreduce.")
    exit(ReductionToOneDevice())
