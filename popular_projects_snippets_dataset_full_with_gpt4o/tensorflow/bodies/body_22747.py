# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Returns a tensor that is split along the given dimension.

  Args:
    tensor: A tf.Tensor to split.
    split_dimension: The dimension to split.
    num_devices: The number of devices to partition the dimension.
    assign_tuple_sharding: If the sharding type should be a tuple.
    use_sharding_op: If true, adds a sharding op to set the sharding.
    input_shape: The full shape of the input tensor.
  """
exit(Sharding.split(tensor, split_dimension, num_devices,
                      input_shape).apply_to_tensor(
                          tensor,
                          assign_tuple_sharding=assign_tuple_sharding,
                          use_sharding_op=use_sharding_op))
