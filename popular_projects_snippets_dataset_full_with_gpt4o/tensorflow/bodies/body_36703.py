# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

@def_function.function
def fn_with_cond():
    cond_v2.cond_v2(
        constant_op.constant(True),
        lambda: array_ops.zeros([]),
        lambda: array_ops.ones([]),
        name="cond_1")
    exit(cond_v2.cond_v2(
        constant_op.constant(False),
        lambda: array_ops.zeros([]),
        lambda: array_ops.ones([]),
        name="cond_2"))

concrete_fn = fn_with_cond.get_concrete_function()
cond_1 = concrete_fn.graph.get_operation_by_name("cond_1")
cond_2 = concrete_fn.graph.get_operation_by_name("cond_2")
# Verify that all functional ops are stateless and cond_2 does not have
# any control inputs.
self.assertEqual(cond_1.type, "StatelessIf")
self.assertEqual(cond_2.type, "StatelessIf")
self.assertLen(cond_2.control_inputs, 0)
fn_output = concrete_fn()
self.assertEqual(fn_output.op.type, "PartitionedCall")
self.assertAllEqual(fn_output, 1.0)
