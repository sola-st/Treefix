# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Adds annotation that `tensor` will be assigned to a logical device.

    This adds an annotation to `tensor` specifying that operations on
    `tensor` will be invoked on logical core device id `logical_device_id`.
    When model parallelism is used, the default behavior is that all ops
    are placed on zero-th logical device.

    ```python

    # Initializing TPU system with 2 logical devices and 4 replicas.
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    topology = tf.tpu.experimental.initialize_tpu_system(resolver)
    device_assignment = tf.tpu.experimental.DeviceAssignment.build(
        topology,
        computation_shape=[1, 1, 1, 2],
        num_replicas=4)
    strategy = tf.distribute.TPUStrategy(
        resolver, experimental_device_assignment=device_assignment)
    iterator = iter(inputs)

    @tf.function()
    def step_fn(inputs):
      output = tf.add(inputs, inputs)

      # Add operation will be executed on logical device 0.
      output = strategy.experimental_assign_to_logical_device(output, 0)
      return output

    strategy.run(step_fn, args=(next(iterator),))
    ```

    Args:
      tensor: Input tensor to annotate.
      logical_device_id: Id of the logical core to which the tensor will be
        assigned.

    Raises:
      ValueError: The logical device id presented is not consistent with total
      number of partitions specified by the device assignment or the TPUStrategy
      is constructed with `experimental_spmd_xla_partitioning=True`.

    Returns:
      Annotated tensor with identical value as `tensor`.
    """
if self.extended._use_spmd_for_xla_partitioning:  # pylint: disable=protected-access
    raise ValueError(
        "Cannot assign a tensor to a logical device in SPMD mode. To disable "
        "SPMD, Please construct the TPUStrategy with "
        "`experimental_spmd_xla_partitioning=False`")

num_logical_devices_per_replica = self.extended._tpu_devices.shape[1]  # pylint: disable=protected-access
if (logical_device_id < 0 or
    logical_device_id >= num_logical_devices_per_replica):
    raise ValueError("`logical_core_id` to assign must be lower then total "
                     "number of logical devices per replica. Received "
                     "logical device id {} but there are only total of {} "
                     "logical devices in replica.".format(
                         logical_device_id, num_logical_devices_per_replica))
exit(xla_sharding.assign_device(
    tensor, logical_device_id, use_sharding_op=True))
