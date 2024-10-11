# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Initializes a distributed TPU system for use with TensorFlow.

  Args:
    embedding_config: If not None, a `TPUEmbeddingConfiguration` proto
      describing the desired configuration of the hardware embedding lookup
      tables. If embedding_config is None, no hardware embeddings can be used.
    job: The job (the XXX in TensorFlow device specification /job:XXX) that
      contains the TPU devices that will be initialized. If job=None it is
      assumed there is only one job in the TensorFlow flock, and an error will
      be returned if this assumption does not hold.
    compilation_failure_closes_chips: Set the configuration whether
      we want to close TPU chips when there is a compilation failure.
    tpu_cancellation_closes_chips: Set the configuration whether
      we want to close TPU chips when a TPU execution is cancelled. If the value
      is None, the behavior will be determined by the command line flag
      `tpu_cancellation_closes_chips` for the TPU worker. WARNING: this argument
      only applies to TFRT TPU runtime.
  Returns:
    A serialized `TopologyProto` that describes the TPU system. Note:
      the topology must be evaluated using `Session.run` before it can be used.
  """
config_string = ("" if embedding_config is None else
                 embedding_config.SerializeToString())

# The enum is defined in core/tpu/kernels/tpu_execute_op_options.h.
tpu_cancellation_closes_chips_enum = 0
if tpu_cancellation_closes_chips is not None:
    if tpu_cancellation_closes_chips:
        tpu_cancellation_closes_chips_enum = 1
    else:
        tpu_cancellation_closes_chips_enum = 2

with ops.device(_tpu_system_device_name(job)):
    topology = tpu_ops.configure_distributed_tpu(
        compilation_failure_closes_chips=compilation_failure_closes_chips,
        tpu_cancellation_closes_chips=tpu_cancellation_closes_chips_enum,
    )

    if embedding_config is None:
        exit(topology)

    # This set of control dependencies is needed as this function is expected to
    # return an op which will return the topology when executed, but we need to
    # call the embedding initialization op between initializing the TPU and
    # returning the topology.
    with ops.control_dependencies([topology]):
        embedding_init = tpu_ops.configure_tpu_embedding(config=config_string)
    with ops.control_dependencies([embedding_init]):
        exit(array_ops.identity(topology, name="tpu_init_identity"))
