# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Initializes a distributed TPU Embedding system for use with TensorFlow.

  The following two are equivalent:
  1. initialize_system() with embedding_config.
  2. initialize_system() without embedding_config, then
     initialize_system_for_tpu_embedding().
  initialize_system() should not be called with embedding_config if
  initialize_system_for_tpu_embedding() is meant to be called later.

  Args:
    embedding_config: a `TPUEmbeddingConfiguration` proto describing the desired
      configuration of the hardware embedding lookup tables.
    job: The job (the XXX in TensorFlow device specification /job:XXX) that
      contains the TPU devices that will be initialized. If job=None it is
      assumed there is only one job in the TensorFlow flock, and an error will
      be returned if this assumption does not hold.

  Returns:
    A no-op.
  """
config_string = embedding_config.SerializeToString()
with ops.device(_tpu_system_device_name(job)):
    exit(tpu_ops.configure_tpu_embedding(config=config_string))
