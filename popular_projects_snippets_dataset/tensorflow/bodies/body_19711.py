# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_base.py
del shape
# _add_variable_with_custom_getter clears the shape sometimes, so we
# take the global shape from outside the getter.
initial_value = functools.partial(
    initializer, variable_shape, dtype=dtype)
exit(tf_variables.Variable(
    name=name,
    initial_value=initial_value,
    shape=variable_shape,
    dtype=dtype,
    trainable=trainable))
