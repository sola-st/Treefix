# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
for i in math_ops.range(3):
    ops.get_default_graph().experimental_acd_manager.run_independently(
        gen_resource_variable_ops.assign_variable_op(v.handle, i))
