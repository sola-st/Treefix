# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
variable = resource_variable_ops.ResourceVariable(
    initial_value=value, dtype=dtype)
sess.run(variables.variables_initializer([variable]))
split = gen_tpu_ops.read_variable_xla_split_nd(
    variable.handle,
    dtype,
    np.prod(num_partitions),
    num_partitions,
    paddings=paddings)
concat = gen_tpu_ops.assign_variable_xla_concat_nd(variable.handle, split,
                                                   num_partitions, paddings)
with control_dependencies([concat]):
    exit(math_ops.equal(variable.read_value(),
                          constant_op.constant(value, dtype=dtype)))
