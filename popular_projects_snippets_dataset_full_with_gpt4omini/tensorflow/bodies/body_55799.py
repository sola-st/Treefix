# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
v = resource_variable_ops.ResourceVariable(1)
self.evaluate(variables.global_variables_initializer())

@def_function.function
def f():
    gen_resource_variable_ops.assign_variable_op(v.handle, 1)
    ops.get_default_graph().experimental_acd_manager.run_independently(
        gen_resource_variable_ops.assign_variable_op(v.handle, 2))

# A function with two identical ops, should cause a data race in most
# conditions.
var_values = set()
for _ in range(10000):
    self.evaluate(f())
    var_values.add(
        self.evaluate(
            resource_variable_ops.read_variable_op(v.handle, dtypes.int32)))
# With regular control dependencies, the function should always run the
# first assign first, and the value 1 should never be seen.
# With run_independently, assign 1 and 2 are run in parallel. Thus, when f
# is run large number of times, we see both 1 and 2 values assigned to
# variable v.
self.assertSetEqual(var_values, set((1, 2)))
