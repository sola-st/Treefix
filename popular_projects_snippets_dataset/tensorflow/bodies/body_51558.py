# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
exit(resource_variable_ops.var_handle_op(
    shape=tensor_shape.as_shape([]),
    dtype=dtypes.float32,
    shared_name="my_var_name",
    name="my_var",
    container="my_container",
))
