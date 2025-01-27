# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Applies this Sharding attribute to `tensor`.

    Args:
      tensor: A tf.Tensor to split.
      assign_tuple_sharding: If the sharding type should be a tuple.
      use_sharding_op: Whether to create a sharding op on `tensor`.
      unspecified_dims: An optional list of dimensions unspecified.

    Returns:
      The tensor with Sharding attribute.
    """
if unspecified_dims:
    assert use_sharding_op and not assign_tuple_sharding
proto = self._proto
if use_sharding_op:
    if assign_tuple_sharding:
        proto = self._create_tuple_proto(num_outputs=1)
        tensor = tf2xla.sharding(tensor, sharding=proto.SerializeToString())
    else:
        tensor = tf2xla.sharding(
            tensor,
            sharding=proto.SerializeToString(),
            unspecified_dims=unspecified_dims or [])
elif assign_tuple_sharding or len(tensor.op.outputs) > 1:
    proto = self._get_or_create_tuple_proto(tensor.op)
    # We can't mutate an element of old_proto.tuple_shardings, so create
    # a new proto.
    tuple_shardings = list(proto.tuple_shardings)
    tuple_shardings[tensor.value_index] = self._proto
    proto = xla_data_pb2.OpSharding(
        type=xla_data_pb2.OpSharding.TUPLE, tuple_shardings=tuple_shardings)

# TODO(jmolloy): This need to be seriously revisited before declaring this
# API available for public use.
# pylint: disable=protected-access
tensor.op._set_attr('_XlaSharding',
                    attr_value_pb2.AttrValue(s=proto.SerializeToString()))
exit(tensor)
