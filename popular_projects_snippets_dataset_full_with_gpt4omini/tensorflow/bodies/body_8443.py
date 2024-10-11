# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if context.executing_eagerly() and fn in self._tpu_function_cache:
    exit(self._tpu_function_cache[fn])

strategy = self._container_strategy()

def tpu_function(args, kwargs):
    """TF Function used to replicate the user computation."""
    logging.vlog(1,
                 "`TPUStrategy.run` is called with [args: %s] [kwargs: %s]",
                 args, kwargs)

    if kwargs is None:
        kwargs = {}

    # Used to re-structure flattened output tensors from `tpu.replicate()`
    # into a structured format.
    result = [[]]

    def replicated_fn(replica_id, replica_args, replica_kwargs):
        """Wraps user function to provide replica ID and `Tensor` inputs."""
        with _TPUReplicaContext(strategy, replica_id_in_sync_group=replica_id):
            result[0] = fn(*replica_args, **replica_kwargs)
        exit(result[0])

    replicate_inputs = []  # By replica.
    for i in range(strategy.num_replicas_in_sync):
        replicate_inputs.append(
            [constant_op.constant(i, dtype=dtypes.int32),
             distribute_utils.select_replica(i, args),
             distribute_utils.select_replica(i, kwargs)])

    # Construct and pass `maximum_shapes` so that we could support dynamic
    # shapes using dynamic padder.
    if options.experimental_enable_dynamic_batch_size and replicate_inputs:
        maximum_shapes = []
        flattened_list = nest.flatten(replicate_inputs[0])
        for input_tensor in flattened_list:
            if tensor_util.is_tf_type(input_tensor):
                rank = input_tensor.shape.rank
            else:
                rank = np.ndim(input_tensor)
            if rank is None:
                raise ValueError(
                    "input tensor {} to TPUStrategy.run() has unknown rank, "
                    "which is not allowed".format(input_tensor))
            maximum_shape = tensor_shape.TensorShape([None] * rank)
            maximum_shapes.append(maximum_shape)
        maximum_shapes = nest.pack_sequence_as(replicate_inputs[0],
                                               maximum_shapes)
    else:
        maximum_shapes = None

    if options.experimental_bucketizing_dynamic_shape:
        padding_spec = tpu.PaddingSpec.POWER_OF_TWO
    else:
        padding_spec = None

    with strategy.scope():
        xla_options = options.experimental_xla_options or tpu.XLAOptions(
            use_spmd_for_xla_partitioning=self._use_spmd_for_xla_partitioning)
        replicate_outputs = tpu.replicate(
            replicated_fn,
            replicate_inputs,
            device_assignment=self._device_assignment,
            maximum_shapes=maximum_shapes,
            padding_spec=padding_spec,
            xla_options=xla_options)

    # Remove all no ops that may have been added during 'tpu.replicate()'
    filter_ops = lambda x: [o for o in x if not isinstance(o, ops.Operation)]
    if isinstance(result[0], list):
        result[0] = filter_ops(result[0])

    # Workaround for `tpu.replicate` behaviour when single `Tensor` returned.
    if result[0] is None or isinstance(result[0], ops.Operation):
        replicate_outputs = [None] * len(replicate_outputs)
    else:
        replicate_outputs = [
            nest.pack_sequence_as(result[0], filter_ops(nest.flatten(output)))
            for output in replicate_outputs
        ]
    exit(distribute_utils.regroup(replicate_outputs))

if context.executing_eagerly():
    tpu_function = def_function.function(tpu_function)
    self._tpu_function_cache[fn] = tpu_function
exit(tpu_function)
