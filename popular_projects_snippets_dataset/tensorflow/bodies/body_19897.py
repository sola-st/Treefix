# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Enqueues id tensors for embedding lookup.

    This function enqueues a structure of features to be looked up in the
    embedding tables. We expect that the input shapes of each of the tensors in
    features matches the output shapes set via FeatureConfig or build method
    (if any). the output shapes will be auto detected based on the input shapes
    with the max_sequence_length or output shape setting in the FeatureConfig.
    Note that the output shapes is based on per replica batch size.
    If your input dataset is batched to the global batch size and you use
    `tf.distribute.TPUStrategy`'s `experimental_distribute_dataset`
    or if you use `distribute_datasets_from_function` and batch
    to the per core batch size computed by the context passed to your input
    function, the output shapes should match automatically.

    The auto detected the output shapes:
      1. For dense tensor, if rank 2 or above, make sure the tensor has last
         dimension as 1. The output shape will be the input shape excluding
         the last dimension.
      2. For sparse tensor, make sure the tensor has rank 2 and above.
           a. If feature config has max_sequence_length equals 0 or output shape
              set (the max_sequence_length setting will be ignored), the
              output shape will be the input shape excluding the last dimension.
           b. Otherwize if the tensor is rank 2, the output shape will be input
              shape  with last dimension set as max_sequence_length. If the
              tensor is above rank 2, the output shape will be the input shape
              excluding the last dimension and the last dimension of the output
              shape will be set to max_sequence_length.
      3. For ragged tensor, make sure the tensor has rank 2.
           a. If feature config has max_sequence_length equals 0 or output shape
              set (the max_sequence_length setting will be ignored), the
              output shape will be the input shape excluding the last dimension.
           b. Otherwise, the output shape will be the input shape excluding the
              last dimension and the last dimension of the output shape will be
              set to max_sequence_length.

    ```python
    strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbedding(...)

    distributed_dataset = (
        strategy.distribute_datasets_from_function(
            dataset_fn=...,
            options=tf.distribute.InputOptions(
                experimental_fetch_to_device=False))
    dataset_iterator = iter(distributed_dataset)

    @tf.function
    def training_step():
      def tpu_step(tpu_features):
        with tf.GradientTape() as tape:
          activations = embedding.dequeue()
          tape.watch(activations)

          loss = ... #  some computation involving activations

        embedding_gradients = tape.gradient(loss, activations)
        embedding.apply_gradients(embedding_gradients)

      embedding_features, tpu_features = next(dataset_iterator)
      embedding.enqueue(embedding_features, training=True)
      strategy.run(tpu_step, args=(tpu_features,))

    training_step()
    ```

    NOTE: You should specify `training=True` when using
    `embedding.apply_gradients` as above and `training=False` when not using
    `embedding.apply_gradients` (e.g. for frozen embeddings or when doing
    evaluation).

    For finer grained control, in the above example the line

    ```
      embedding.enqueue(embedding_features, training=True)
    ```

    may be replaced with

    ```
      per_core_embedding_features = self.strategy.experimental_local_results(
          embedding_features)

      def per_core_enqueue(ctx):
        core_id = ctx.replica_id_in_sync_group
        device = strategy.extended.worker_devices[core_id]
        embedding.enqueue(per_core_embedding_features[core_id],
                          device=device)

      strategy.experimental_distribute_values_from_function(
          per_core_queue_inputs)
    ```

    Args:
      features: A nested structure of `tf.Tensor`s, `tf.SparseTensor`s or
        `tf.RaggedTensor`s, with the same structure as `feature_config`. Inputs
        will be downcast to `tf.int32`. Only one type out of `tf.SparseTensor`
        or `tf.RaggedTensor` is supported per call.
      weights: If not `None`, a nested structure of `tf.Tensor`s,
        `tf.SparseTensor`s or `tf.RaggedTensor`s, matching the above, except
        that the tensors should be of float type (and they will be downcast to
        `tf.float32`). For `tf.SparseTensor`s we assume the `indices` are the
        same for the parallel entries from `features` and similarly for
        `tf.RaggedTensor`s we assume the row_splits are the same.
      training: Defaults to `True`. If `False`, enqueue the batch as inference
        batch (forward pass only). Do not call `apply_gradients` when this is
        `False` as this may lead to a deadlock.
       name: A name for the underlying op.
       device: The device name (e.g. '/task:0/device:TPU:2') where this batch
         should be enqueued. This should be set if and only if features is not a
         `tf.distribute.DistributedValues` and enqueue is not being called
         inside a TPU context (e.g. inside `TPUStrategy.run`).

    Raises:
      ValueError: When called inside a strategy.run call and input is not
        directly taken from the args of the `strategy.run` call. Also if
        the size of any sequence in `features` does not match corresponding
        sequence in `feature_config`. Similarly for `weights`, if not `None`.
        If input shapes of features is unequal or different from a previous
        call.
      RuntimeError: When called inside a strategy.run call and inside XLA
        control flow. If batch_size is not able to be determined and build was
        not called.
      TypeError: If the type of any sequence in `features` does not match
        corresponding sequence in `feature_config`. Similarly for `weights`, if
        not `None`.
    """
if not self._using_tpu:
    raise RuntimeError("enqueue is not valid when TPUEmbedding object is not "
                       "created under a TPUStrategy.")

in_tpu_context = self._raise_error_for_incorrect_control_flow_context()

nest.assert_same_structure(self._feature_config, features)

if not self._verify_output_shapes_on_enqueue:
    if not self._output_shapes or not self._built:
        raise ValueError(
            "Configured not to check output shapes on each enqueue() call; please "
            "ensure build() was called with output shapes to initialize "
            "the TPU for embeddings.")
else:
    input_shapes = self._get_input_shapes(features, in_tpu_context)

    self._maybe_build(input_shapes)
    # If is already built, we still need to check if the output shapes matches
    # with the previous ones.
    self._check_output_shapes(
        self._get_output_shapes_from_input_shapes(input_shapes))

flat_inputs = nest.flatten(features)
flat_weights = [None] * len(flat_inputs)
if weights is not None:
    nest.assert_same_structure(self._feature_config, weights)
    flat_weights = nest.flatten(weights)
flat_features = nest.flatten_with_joined_string_paths(self._feature_config)
flat_paths, _ = zip(*flat_features)

self._raise_error_for_inputs_not_on_cpu(flat_inputs, flat_paths)
# If we are in a tpu_context, automatically apply outside compilation.
if in_tpu_context:
    self._raise_error_for_non_direct_inputs(features)

    def generate_enqueue_ops():
        """Generate enqueue ops for outside compilation."""
        # Note that we put array_ops.where_v2 rather than a python if so that
        # the op is explicitly create and the constant ops are both in the graph
        # even though we don't expect training to be a tensor (and thus generate
        # control flow automatically). This need to make it easier to re-write
        # the graph later if we need to fix which mode needs to be used.
        mode_override = array_ops.where_v2(training,
                                           constant_op.constant("train"),
                                           constant_op.constant("inference"))
        # Device ordinal is -1 here, a later rewrite will fix this once the op
        # is expanded by outside compilation.
        enqueue_op = self._generate_enqueue_op(
            flat_inputs, flat_weights, flat_features, device_ordinal=-1,
            mode_override=mode_override)

        # Apply the name tag to the op.
        if name is not None:
            _add_key_attr(enqueue_op, name)

    tpu.outside_compilation(generate_enqueue_ops)

elif device is None:
    mode_override = "train" if training else "inference"
    # We generate enqueue ops per device, so we need to gather the all
    # features for a single device in to a dict.
    # We rely here on the fact that the devices in the PerReplica value occur
    # in the same (standard) order as self._strategy.extended.worker_devices.
    enqueue_ops = []
    for replica_id in range(self._strategy.num_replicas_in_sync):
        replica_inputs = distribute_utils.select_replica(replica_id,
                                                         flat_inputs)
        replica_weights = distribute_utils.select_replica(replica_id,
                                                          flat_weights)
        tpu_device = self._strategy.extended.worker_devices[replica_id]
        # TPU devices string are like /job:worker/replica:0/task:0/device:TPU:0
        # the device ordinal is the last number
        device_ordinal = (
            tf_device.DeviceSpec.from_string(tpu_device).device_index)

        with ops.device(device_util.get_host_for_device(tpu_device)):
            enqueue_op = self._generate_enqueue_op(
                replica_inputs, replica_weights, flat_features,
                device_ordinal=device_ordinal, mode_override=mode_override)

            # Apply the name tag to the op.
            if name is not None:
                _add_key_attr(enqueue_op, name)
            enqueue_ops.append(enqueue_op)
else:
    mode_override = "train" if training else "inference"
    device_spec = tf_device.DeviceSpec.from_string(device)
    if device_spec.device_type != "TPU":
        raise ValueError(
            "Non-TPU device {} passed to enqueue.".format(device))

    with ops.device(device_util.get_host_for_device(device)):
        enqueue_op = self._generate_enqueue_op(
            flat_inputs, flat_weights, flat_features,
            device_ordinal=device_spec.device_index,
            mode_override=mode_override)

        # Apply the name tag to the op.
        if name is not None:
            _add_key_attr(enqueue_op, name)
