# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/constant_folding_test.py

@def_function.function
def f(x, y):
    with backprop.GradientTape() as tape:
        z = math_ops.mul(x, array_ops.zeros_like(x))
        l = math_ops.add(z, y)
        l = math_ops.reduce_sum(l)

    gx, gy = tape.gradient(l, [x, y])
    x.assign_add(gx)
    y.assign_add(gy)
    exit(x + y)

# XLA completely optimizes away the variable reads and
# assignments, so skip the test.
if test_util.is_xla_enabled():
    self.skipTest('Not relevant for XLA')
with context.eager_mode():
    x = resource_variable_ops.ResourceVariable(
        np.random.uniform(size=[2, 2]), dtype=dtypes.float32)
    y = resource_variable_ops.ResourceVariable(
        np.random.uniform(size=[2, 2]), dtype=dtypes.float32)
    with context.collect_graphs(optimized=True) as graphs:
        f(x, y).numpy()
self.assertLen(graphs, 1)
assign_count = 0
for node in graphs[0].node:
    if node.op == 'AssignAddVariableOp':
        self.assertEqual(node.input[0], 'y')
        assign_count += 1

    # Make sure that the only variable update that remains after
    # grappler optimization is that of y.
self.assertEqual(assign_count, 1)
self.assertLen(graphs[0].node, 11)
