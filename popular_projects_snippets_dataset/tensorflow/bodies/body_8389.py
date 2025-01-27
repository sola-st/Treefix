# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Adds annotation that `tensor` will be split across logical devices.

    This adds an annotation to tensor `tensor` specifying that operations on
    `tensor` will be split among multiple logical devices. Tensor `tensor` will
    be split across dimensions specified by `partition_dimensions`.
    The dimensions of `tensor` must be divisible by corresponding value in
    `partition_dimensions`.

    For example, for system with 8 logical devices, if `tensor` is an image
    tensor with shape (batch_size, width, height, channel) and
    `partition_dimensions` is [1, 2, 4, 1], then `tensor` will be split
    2 in width dimension and 4 way in height dimension and the split
    tensor values will be fed into 8 logical devices.

    ```python
    # Initializing TPU system with 8 logical devices and 1 replica.
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    topology = tf.tpu.experimental.initialize_tpu_system(resolver)
    device_assignment = tf.tpu.experimental.DeviceAssignment.build(
        topology,
        computation_shape=[1, 2, 2, 2],
        num_replicas=1)
    # Construct the TPUStrategy. Since we are going to split the image across
    # logical devices, here we set `experimental_spmd_xla_partitioning=True`
    # so that the partitioning can be compiled in SPMD mode, which usually
    # results in faster compilation and smaller HBM requirement if the size of
    # input and activation tensors are much bigger than that of the model
    # parameters. Note that this flag is suggested but not a hard requirement
    # for `experimental_split_to_logical_devices`.
    strategy = tf.distribute.TPUStrategy(
        resolver, experimental_device_assignment=device_assignment,
        experimental_spmd_xla_partitioning=True)

    iterator = iter(inputs)

    @tf.function()
    def step_fn(inputs):
      inputs = strategy.experimental_split_to_logical_devices(
        inputs, [1, 2, 4, 1])

      # model() function will be executed on 8 logical devices with `inputs`
      # split 2 * 4  ways.
      output = model(inputs)
      return output

    strategy.run(step_fn, args=(next(iterator),))
    ```
    Args:
      tensor: Input tensor to annotate.
      partition_dimensions: An unnested list of integers with the size equal to
        rank of `tensor` specifying how `tensor` will be partitioned. The
        product of all elements in `partition_dimensions` must be equal to the
        total number of logical devices per replica.

    Raises:
      ValueError: 1) If the size of partition_dimensions does not equal to rank
        of `tensor` or 2) if product of elements of `partition_dimensions` does
        not match the number of logical devices per replica defined by the
        implementing DistributionStrategy's device specification or
        3) if a known size of `tensor` is not divisible by corresponding
        value in `partition_dimensions`.

    Returns:
      Annotated tensor with identical value as `tensor`.
    """
num_logical_devices_per_replica = self.extended._tpu_devices.shape[1]  # pylint: disable=protected-access
num_partition_splits = np.prod(partition_dimensions)
input_shape = tensor.shape
tensor_rank = len(input_shape)

if tensor_rank != len(partition_dimensions):
    raise ValueError("Length of `partition_dimensions` must equal to the "
                     "rank of `tensor.shape` ({}). Received "
                     "len(partition_dimensions)={}.".format(
                         tensor_rank, len(partition_dimensions)))

for dim_index, dim_size in enumerate(input_shape):
    if dim_size is None:
        continue

    split_size = partition_dimensions[dim_index]
    if dim_size % split_size != 0:
        raise ValueError("Tensor shape at `partition_dimensions[{}]` must be "
                         "divisible by corresponding value specified "
                         "by `partition_dimensions` ({}). Received: {}.".format(
                             dim_index, split_size, dim_size))

if num_partition_splits != num_logical_devices_per_replica:
    raise ValueError(
        "The product of `partition_dimensions` should be the same as the "
        "number of logical devices (={}). Received `partition_dimensions`={},"
        "and their product is {}.".format(num_logical_devices_per_replica,
                                          partition_dimensions,
                                          num_partition_splits))

tile_assignment = np.arange(num_partition_splits).reshape(
    partition_dimensions)
exit(xla_sharding.tile(tensor, tile_assignment, use_sharding_op=True))
