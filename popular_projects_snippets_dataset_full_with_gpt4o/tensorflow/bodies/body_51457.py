# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
weight.read_value()  # Just get the tape to watch the variable
handle = array_ops.identity(weight.handle)

@def_function.function
def launder_var_handle():
    exit(array_ops.identity(handle))

exit(x + resource_variable_ops.read_variable_op(
    launder_var_handle(), dtypes.float32
))
