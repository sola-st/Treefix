# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
data = array_ops.stack([b"data"])
buffer_var = variables.VariableV1(
    initial_value=array_ops.zeros(shape=(), dtype=dtypes.string),
    trainable=False,
    collections=[ops.GraphKeys.LOCAL_VARIABLES],
    name="buffer",
    dtype=dtypes.string,
    validate_shape=False,
    use_resource=False)
result = state_ops.assign(buffer_var, data, validate_shape=False)
with self.cached_session() as sess:
    sess.run(variables.local_variables_initializer())
    self.assertEqual(result.eval(), b"data")
