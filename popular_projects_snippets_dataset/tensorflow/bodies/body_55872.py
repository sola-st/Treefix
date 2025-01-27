# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py

@def_function.function
def fn_with_write():
    gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)
    exit(gen_resource_variable_ops.read_variable_op(v.handle, v.dtype))

exit(fn_with_write())
