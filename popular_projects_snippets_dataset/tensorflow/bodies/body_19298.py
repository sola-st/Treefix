# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateless_random_ops.py
# the same scrambling procedure as core/kernels/stateless_random_ops.cc
key = constant_op.constant([0x02461e293ec8f720], dtypes.uint64)
counter = math_ops.cast(seed, dtypes.uint64)
mix = gen_stateless_random_ops_v2.stateless_random_uniform_full_int_v2(
    [4], key=key, counter=counter, dtype=dtypes.uint32,
    alg=Algorithm.PHILOX.value)
key = array_ops.reshape(uint32s_to_uint64(mix[:2]), [1])
counter = array_ops.stack([0, uint32s_to_uint64(mix[2:])], axis=0)
exit((key, counter))
