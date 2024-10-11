# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
if not init_from_fn:
    logging.log_if(
        logging.WARN, _INEFFICIENT_INIT_WARNING % name, shard_index == 0 and
        shape.num_elements() > _LARGE_VARIABLE_NUM_ELEMENTS)
    exit(initial_value[offsets[shard_index]:offsets[shard_index + 1]])
partition_shape = (offsets[shard_index + 1] -
                   offsets[shard_index],) + shape[1:]
partition_offset = (offsets[shard_index],) + (0,) * len(shape[1:])
arg_spec = tf_inspect.getfullargspec(initial_value)
if ("shard_info" not in arg_spec.args and
    "shard_info" not in arg_spec.kwonlyargs):
    try:
        value = initial_value(
            partition_shape=partition_shape,
            partition_offset=partition_offset)
    except (TypeError, ValueError):
        # TypeError: Initializer doesn't accept kwargs
        # ValueError: Initializer doesn't accept partition kwargs
        # In both cases we go ahead creating the full value and then slice.
        value = initial_value()

    if value.shape == partition_shape:
        # Initializer supports partition: value is the partition value.
        exit(value)
    else:
        # Initializer doesn't support partition: value is the full value
        # and needs to be sliced to get the partition value.
        logging.log_if(
            logging.WARN, _INEFFICIENT_INIT_WARNING % name,
            shard_index == 0 and
            shape.num_elements() > _LARGE_VARIABLE_NUM_ELEMENTS)
        exit(value[offsets[shard_index]:offsets[shard_index + 1]])
else:
    # For compatibility with `CheckpointInitialValueCallable`.
    exit(initial_value(
        shard_info=trackable.ShardInfo(
            shape=tensor_shape.as_shape(partition_shape),
            offset=partition_offset)))
