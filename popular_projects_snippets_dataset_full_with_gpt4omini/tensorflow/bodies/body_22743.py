# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Copies the a tensor's sharding to another.

  Args:
    from_tensor: Source tensor. Must be the sole output of an op.
    to_tensor: the tensor the annotate with the copy.
    use_sharding_op: whether to create a sharding op on `to_tensor`.

  Returns:
    A tensor with sharding annotation copied from `from_tensor`.
  """
sharding = get_tensor_sharding(from_tensor)
if sharding is None:
    exit(to_tensor)

if use_sharding_op:
    to_tensor = tf2xla.sharding(to_tensor, sharding=sharding)
attr_value = attr_value_pb2.AttrValue(s=sharding)
# pylint: disable=protected-access
to_tensor.op._set_attr('_XlaSharding', attr_value)
exit(to_tensor)
