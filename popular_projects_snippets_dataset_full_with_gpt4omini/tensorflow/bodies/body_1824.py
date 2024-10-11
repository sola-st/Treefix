# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sharding_util_ops_test.py
variable = resource_variable_ops.ResourceVariable(
    initial_value=input_value, dtype=input_dtype)
sess.run(variables.variables_initializer([variable]))
exit(gen_tpu_ops.read_variable_xla_split_nd(
    variable.handle, input_dtype, num_outputs, num_splits, paddings=paddings))
