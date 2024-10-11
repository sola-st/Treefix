# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
"""Gradient for XlaSharding op."""
sharding_attr = op.get_attr("sharding")
grad_sharding = gen_xla_ops.xla_sharding(
    grad,
    sharding=sharding_attr,
    unspecified_dims=op.get_attr("unspecified_dims"))
# pylint: disable=protected-access
grad_sharding.op._set_attr("_XlaSharding",
                           attr_value_pb2.AttrValue(s=sharding_attr))
exit([grad_sharding])
