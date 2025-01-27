# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Create the underlying variables and initializes the TPU for embeddings.

    This method creates the underlying variables (including slot variables). If
    created under a TPUStrategy, this will also initialize the TPU for
    embeddings.

    This function will automatically get called by enqueue, which will try to
    determine your output shapes. If this fails, you must manually
    call this method before you call enqueue.

    Args:
      per_replica_input_shapes: A nested structure of The per replica input
        shapes that matches the structure of the feature config. The input
        shapes should be the same as the input shape of the feature (except for
        ragged tensor) Note that it is fixed and the same per replica input
        shapes must be used for both training and evaluation. If you want to
        calculate this from the global input shapes, you can use
        `num_replicas_in_sync` property of your strategy object. May be set to
        None if not created under a TPUStrategy.
      per_replica_batch_size: (Deprecated) The per replica batch size that you
        intend to use. Note that is fixed and the same batch size must be used
        for both training and evaluation. If you want to calculate this from the
        global batch size, you can use `num_replicas_in_sync` property of your
        strategy object. May be set to None if not created under a TPUStrategy.

    Raises:
      ValueError: If per_replica_input_shapes is inconsistent with the output
      shapes stored in the feature config or the output shapes get from the
      input shapes are not fully defined.
      RuntimeError: If tpu embedding is already initialized on TPU.
    """
if self._built:
    exit()

if self._using_tpu:
    # If the tpu embedding is already initialized on TPU, raise runtime error.
    # Below logic is not added in `initialize_system_for_tpu_embedding`
    # because doing exception control flow in graph mode is difficult.
    if tpu_ops.is_tpu_embedding_initialized():
        raise RuntimeError(
            "TPU is already initialized for embeddings. This may be caused by "
            "using multiple TPUEmbedding instances in a TPU scope which is "
            "unsupported")
    self._get_and_update_output_shapes_from_input(per_replica_input_shapes,
                                                  per_replica_batch_size)

    self._config_proto = self._create_config_proto()

    logging.info("Initializing TPU Embedding engine.")
    tpu_embedding_v2_utils.log_tpu_embedding_configuration(self._config_proto)

    @def_function.function
    def load_config():
        tpu.initialize_system_for_tpu_embedding(self._config_proto)

    load_config()
    logging.info("Done initializing TPU Embedding engine.")

# Create and load variables and slot variables into the TPU.
# Note that this is a dict of dicts. Keys to the first dict are table names.
# We would prefer to use TableConfigs, but then these variables won't be
# properly tracked by the tracking API.
self._variables = self._create_variables_and_slots()

self._built = True

# This is internally conditioned self._built and self._using_tpu
self._load_variables()
