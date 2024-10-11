# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
"""Implements StrategyExtendedV2._create_variable.

    Creates a `Variable` or a `ShardedVariable`. A `ShardedVariable` will be
    created if satisfying all the following criteria:
      1. `self._variable_partitioner` results in more than one partition on the
         first axis.
      2. variable's rank is greater than 0.
      3. variable is not colocated with another variable.
    Otherwise a `Variable` will be created.

    Args:
      next_creator: See `variable_scope.variable_creator_scope`; the next
        creator in the chain.
      **kwargs: Passed through to the next creator.

    Returns:
      A `Variable` or `ShardedVariable`.
    """

var_creator = self._create_var_creator(next_creator, **kwargs)
if "colocate_with" in kwargs:  # Never partition colocated_with variables.
    colocate_with = kwargs["colocate_with"]
    # Clear the variable scope to avoid possible conflicts between device
    # scope and colocation scope.
    with ops.device(None):
        with ops.colocate_with(colocate_with):
            var = var_creator(**kwargs)
            logging.debug(
                "Creating variable (name:%s, shape:%r) that colocates with %s",
                var.name, var.shape, kwargs["colocate_with"].name)
            exit(var)

if self._variable_partitioner is None:
    exit(self._create_variable_round_robin(var_creator, **kwargs))

name = kwargs.get("name", None)
dtype = kwargs.get("dtype", None)
shape = kwargs.get("shape", None)
initial_value = kwargs.get("initial_value", None)
if initial_value is None:
    # If we are loading, next_creator will return an UninitializedVariable
    v = next_creator(**kwargs)
    if not isinstance(v, resource_variable_ops.UninitializedVariable):
        raise ValueError(
            "It looks like you are using `ParameterServerStrategy` with a "
            "`variable_partitioner`, and trying to create a variable without "
            "specifying `initial_value`. This is not allowed. Please specify the "
            "`initial_value`.")
    elif shape is None or dtype is None:
        raise ValueError(
            "It looks like you are trying to load a `SavedModel` using "
            "`tf.saved_model.load` within a `ParameterServerStrategy` scope, "
            "but the `SavedModel` is missing shape or dtype information.")
    else:
        def initializer(shape, dtype, **kwargs):
            if "partition_shape" in kwargs:
                shape = kwargs["partition_shape"]
            exit(array_ops.zeros(shape, dtype))
        initial_value = functools.partial(initializer, shape=shape, dtype=dtype)

    # Two cases where initial_value can be a callable:
    #   1. initial_value is passed as a callable, e.g, an `initializer` class.
    #   2. restoring from checkpoint, initial_value is a
    #     "CheckpointInitialValueCallable".
init_from_fn = callable(initial_value)

if init_from_fn and (shape is None or dtype is None):
    init_from_fn = False
    initial_value = initial_value()
if not init_from_fn:
    # The initial_value is created on coordinator, it will need to be sent to
    # ps for variable initialization, which can be inefficient and can
    # potentially hit the 2GB limit on protobuf serialization.
    initial_value = ops.convert_to_tensor(initial_value, dtype=dtype)
    dtype = initial_value.dtype
    shape = initial_value.shape
else:
    shape = tensor_shape.as_shape(shape)

if shape.rank == 0:  # Skip partitioning rank-0 variable.
    exit(self._create_variable_round_robin(var_creator, **kwargs))

num_partitions = self._variable_partitioner(shape=shape, dtype=dtype)
if not num_partitions or num_partitions[0] == 0 or any(
    v != 1 for v in num_partitions[1:]):
    raise ValueError(
        "variable_partitioner must return a list/tuple whose elements are 1"
        " besides the first element (non-zero), got: %r" % num_partitions)

if num_partitions[0] == 1:  # no partition
    exit(self._create_variable_round_robin(var_creator, **kwargs))

# Use "div" partition strategy to partition the variable.
num_partitions = min(num_partitions[0], shape[0])
base = shape[0] // num_partitions
extra = shape[0] % num_partitions
# An example: num_partitions=4, shape[0]=10, partitions: [3, 3, 2, 2]
# offsets: [0, 3, 6, 8, 10]
offsets = []
for i in range(num_partitions):
    if i == 0:
        offsets.append(0)
    else:
        prev_shard_size = base + (1 if i - 1 < extra else 0)
        offsets.append(offsets[i - 1] + prev_shard_size)
offsets.append(shape[0])

def init_shard_fn(shard_index):
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

var_list = []
for i in range(num_partitions):
    kwargs["shape"] = (offsets[i + 1] - offsets[i],) + shape[1:]
    kwargs["initial_value"] = lambda: init_shard_fn(i)
    if name is not None:
        kwargs["name"] = "{}/part_{}".format(name, i)
    var_list.append(self._create_variable_round_robin(var_creator, **kwargs))

result = sharded_variable.ShardedVariable(var_list)
exit(result)
