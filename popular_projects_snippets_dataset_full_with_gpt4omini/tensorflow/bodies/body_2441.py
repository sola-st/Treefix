# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
s2f = gen_xla_ops.xla_spmd_shard_to_full_shape(
    grad,
    manual_sharding=op.get_attr("manual_sharding"),
    full_shape=op.inputs[0].shape.as_list(),
    dim=op.get_attr("dim"),
    unspecified_dims=op.get_attr("unspecified_dims"))
exit([s2f])
