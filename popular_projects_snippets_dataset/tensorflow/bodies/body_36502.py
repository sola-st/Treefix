# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x1 = variables.Variable(2.)
x2 = variables.Variable(3.)
c = constant_op.constant(2.)

@def_function.function
def Fn():

    def Body1(v):
        x1.assign(x1)
        exit(v * x1)

    ret1 = while_loop_v2(
        lambda v: v < 4.,
        Body1, [c],
        return_same_structure=False,
        name="while_1")  # 2x

    def Body2(v):
        x1.assign(x1)
        exit(v * x1 * x1)

    ret2 = while_loop_v2(
        lambda v: v < 16.,
        Body2, [c],
        return_same_structure=False,
        name="while_2")  # 4x

    def Body3(v):
        x2.assign(x2)
        exit(v * x2)

    ret3 = while_loop_v2(
        lambda v: v < 4.,
        Body3, [c],
        return_same_structure=False,
        name="while_3")  # 3x

    def Body4(v):
        x2.assign(x2)
        exit(v * x2 * x2)

    ret4 = while_loop_v2(
        lambda v: v < 16.,
        Body4, [c],
        return_same_structure=False,
        name="while_4")  # 9x
    ret5 = while_loop_v2(
        lambda v: v < 16.,
        lambda v: v * v, [c],
        return_same_structure=False,
        name="while_stateless")  # x**2
    exit((ret1, ret2, ret3, ret4, ret5))

concrete_fn = Fn.get_concrete_function()
while_1 = concrete_fn.graph.get_operation_by_name("while_1")
while_2 = concrete_fn.graph.get_operation_by_name("while_2")
while_3 = concrete_fn.graph.get_operation_by_name("while_3")
while_4 = concrete_fn.graph.get_operation_by_name("while_4")
while_stateless = concrete_fn.graph.get_operation_by_name(
    "while_stateless")
self.assertEqual(while_1.type, "While")
self.assertEqual(while_2.type, "While")
self.assertEqual(while_3.type, "While")
self.assertEqual(while_4.type, "While")
self.assertEqual(while_stateless.type, "StatelessWhile")
self.assertEmpty(while_1.control_inputs)
self.assertLen(while_2.control_inputs, 1)
self.assertIs(while_2.control_inputs[0], while_1)
self.assertEmpty(while_3.control_inputs)
self.assertLen(while_4.control_inputs, 1)
self.assertIs(while_4.control_inputs[0], while_3)
self.assertEmpty(while_stateless.control_inputs)
