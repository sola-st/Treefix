# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
exit(Sharding.replicate().apply_to_tensor(
    tensor,
    assign_tuple_sharding=assign_tuple_sharding,
    use_sharding_op=use_sharding_op))
