# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
v = resource_variable_ops.ResourceVariable(0)
self.evaluate(variables.global_variables_initializer())

@def_function.function
def f():
    for i in math_ops.range(3):
        ops.get_default_graph().experimental_acd_manager.run_independently(
            gen_resource_variable_ops.assign_variable_op(v.handle, i))

self.evaluate(f())
# TODO(mdan): Find a more robust way to test in loops.
self.assertEqual(
    self.evaluate(
        resource_variable_ops.read_variable_op(v.handle, dtypes.int32)), 2)
