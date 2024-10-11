# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
v1 = variables.Variable(2.)
v2 = variables.Variable(4.)

self.evaluate(variables.global_variables_initializer())

@def_function.function
def fn_with_cond():

    def update_v1():
        v1.assign(v1)
        exit(v1)

    def update_v2():
        v2.assign(v2)
        exit(v2)

    cond_v2.cond_v2(
        constant_op.constant(True),
        update_v1,
        lambda: constant_op.constant(0.),
        name="cond_1")
    cond_2 = cond_v2.cond_v2(
        constant_op.constant(False),
        lambda: constant_op.constant(0.),
        update_v1,
        name="cond_2")
    cond_v2.cond_v2(
        constant_op.constant(True),
        update_v2,
        lambda: constant_op.constant(0.),
        name="cond_3")

    @def_function.function
    def cond_4_false_branch():
        v2.assign(v2)
        exit(v2)

    cond_4 = cond_v2.cond_v2(
        constant_op.constant(False),
        lambda: constant_op.constant(0.),
        cond_4_false_branch,
        name="cond_4")
    exit((cond_2, cond_4))

concrete_fn = fn_with_cond.get_concrete_function()
cond_1 = concrete_fn.graph.get_operation_by_name("cond_1")
cond_2 = concrete_fn.graph.get_operation_by_name("cond_2")
cond_3 = concrete_fn.graph.get_operation_by_name("cond_3")
cond_4 = concrete_fn.graph.get_operation_by_name("cond_4")
self.assertEqual(cond_1.type, "If")
self.assertEqual(cond_2.type, "If")
self.assertEqual(cond_3.type, "If")
self.assertEqual(cond_4.type, "If")
self.assertEmpty(cond_1.control_inputs)
self.assertLen(cond_2.control_inputs, 1)
self.assertIs(cond_2.control_inputs[0], cond_1)
self.assertEmpty(cond_3.control_inputs)
self.assertLen(cond_4.control_inputs, 1)
self.assertIs(cond_4.control_inputs[0], cond_3)
_, cond_4_false_graph = cond_v2.get_func_graphs(cond_4)
cond_4_false_graph_operations = cond_4_false_graph.get_operations()
self.assertEmpty([
    op for op in cond_4_false_graph_operations
    if op.type == "PartitionedCall"
])
self.assertLen([
    op for op in cond_4_false_graph_operations
    if op.type == "StatefulPartitionedCall"
], 1)
fn_output = concrete_fn()
self.assertEqual(fn_output[0].op.type, "StatefulPartitionedCall")
self.assertAllEqual(self.evaluate(fn_output), [2.0, 4.0])
