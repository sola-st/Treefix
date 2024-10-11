# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
del sess

const_input_op = constant_op.constant(value, dtype=dtype)
split = gen_tpu_ops.xla_split_nd(
    const_input_op,
    np.prod(num_partitions),
    num_partitions,
    paddings=paddings)
concat = gen_tpu_ops.xla_concat_nd(split, num_partitions, paddings)
exit(math_ops.equal(const_input_op, concat))
