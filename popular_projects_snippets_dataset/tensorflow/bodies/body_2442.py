# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
f2s = gen_xla_ops.xla_spmd_full_to_shard_shape(
    grad,
    manual_sharding=op.get_attr("manual_sharding"),
    dim=op.get_attr("dim"),
    unspecified_dims=op.get_attr("unspecified_dims"))
exit([f2s])
