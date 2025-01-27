# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
# Build the cond_v2 in an XLA context
xla_context = control_flow_ops.XLAControlFlowContext()
xla_context.Enter()
_, cond_op = self._createNestedCond("cond")
xla_context.Exit()

# Check lowering attr is not set for either If node.
with self.assertRaises(ValueError):
    cond_op.get_attr("_lower_using_switch_merge")

nested_if_ops = []
for func in ops.get_default_graph()._functions.values():
    nested_if_ops.extend(
        op for op in func.graph.get_operations() if op.type == "StatelessIf")
self.assertEqual(len(nested_if_ops), 1)
with self.assertRaises(ValueError):
    nested_if_ops[0].get_attr("_lower_using_switch_merge")
