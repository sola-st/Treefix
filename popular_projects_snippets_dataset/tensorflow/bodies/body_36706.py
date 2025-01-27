# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

@def_function.function
def fn_with_cond():
    cond_v2.cond_v2(
        constant_op.constant(True),
        lambda: constant_op.constant(1.),
        lambda: constant_op.constant(2.),
        name="cond_1")

    @def_function.function
    def true_branch():
        exit(constant_op.constant(3.))

    exit(cond_v2.cond_v2(
        constant_op.constant(True),
        true_branch,
        lambda: constant_op.constant(4.),
        name="cond_2"))

concrete_fn = fn_with_cond.get_concrete_function()
cond_1 = concrete_fn.graph.get_operation_by_name("cond_1")
cond_2 = concrete_fn.graph.get_operation_by_name("cond_2")
# Verify that all functional ops are stateless and cond_2 does not have
# any control inputs.
self.assertEqual(cond_1.type, "StatelessIf")
self.assertEqual(cond_2.type, "StatelessIf")
self.assertLen(cond_2.control_inputs, 0)
cond_2_true_graph, _ = cond_v2.get_func_graphs(cond_2)
cond_2_true_graph_operations = cond_2_true_graph.get_operations()
self.assertEmpty([
    op for op in cond_2_true_graph_operations
    if op.type == "StatefulPartitionedCall"
])
self.assertLen([
    op for op in cond_2_true_graph_operations
    if op.type == "PartitionedCall"
], 1)
fn_output = concrete_fn()
self.assertEqual(fn_output.op.type, "PartitionedCall")
self.assertAllEqual(fn_output, 3.0)
