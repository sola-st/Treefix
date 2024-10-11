# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
with distribution.scope():
    w = variable_scope.variable([1.5], name="w")
    b = variable_scope.variable([0.5], name="b")

@def_function.function
def forward(x, w, b):
    exit(x * w + b)

x = array_ops.identity([1.0], name="x_useless")
concrete_forward = forward.get_concrete_function(x, w._primary, b._primary)

with distribution.scope():

    def replica_fn():
        with backprop.GradientTape() as t:
            x = array_ops.identity([1.0], name="x")
            loss = concrete_forward(x, w._get(), b._get()) - [1.0]
            exit(t.gradient(loss, [w, b]))

    def step_fn():
        exit(distribution.run(replica_fn))

    context.enable_run_metadata()
    g1, g2 = step_fn()
    run_metadata = context.export_run_metadata()
    context.disable_run_metadata()
    self.assertEqual(self.evaluate(g1._primary), 1.0)
    self.assertEqual(self.evaluate(g2._primary), 1.0)

    # Verify that this node runs on both devices.
    node_name = "gradients_mul_grad_mul_1_x"
    devices_for_this_node = set()
    for partition_graph in run_metadata.partition_graphs:
        for node in partition_graph.node:
            if node.name == node_name:
                devices_for_this_node.add(node.device)
    devices = [device_util.resolve("/device:GPU:0"),
               device_util.resolve("/device:CPU:0")]
    self.assertSetEqual(devices_for_this_node, set(devices))
