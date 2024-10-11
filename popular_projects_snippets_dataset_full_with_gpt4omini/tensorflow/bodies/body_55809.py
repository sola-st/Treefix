# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
gen_resource_variable_ops.read_variable_op(
    v.handle, v.dtype, name="read1")

result = build_functional_op(v)
gen_resource_variable_ops.read_variable_op(
    v.handle, v.dtype, name="read2")
gen_resource_variable_ops.assign_variable_op(v.handle, v + 1)
exit(result)
