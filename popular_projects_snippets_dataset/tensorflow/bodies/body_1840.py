# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
variable_shape = [] if output_shape is None else output_shape
variable = resource_variable_ops.ResourceVariable(
    initial_value=np.zeros(variable_shape, dtype=input_dtype),
    dtype=input_dtype)
sess.run(variables.variables_initializer([variable]))
const_input_ops = [
    constant_op.constant(i, dtype=input_dtype) for i in input_values
]
concat = gen_tpu_ops.assign_variable_xla_concat_nd(variable.handle,
                                                   const_input_ops,
                                                   num_concats, paddings)
with control_dependencies([concat]):
    exit(variable.read_value())
