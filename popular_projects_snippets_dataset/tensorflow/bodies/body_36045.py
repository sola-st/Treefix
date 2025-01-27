# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(initial_value=1.0)
def cond(i, unused_x):
    exit(i < 1)

def body(i, x):
    def true():
        exit(x + v)
    def false():
        exit(2.0 * v)
    exit((i + 1, control_flow_ops.cond(i > 0, true, false)))

_, x = control_flow_ops.while_loop(cond, body, [0, 0.0])
# Computing gradients does not produce an exception:
g = gradients_impl.gradients(x, v)
self.evaluate(variables.global_variables_initializer())
# Only the false branch is taken so the gradient is 2.
self.assertAllEqual(g[0], 2.0)
