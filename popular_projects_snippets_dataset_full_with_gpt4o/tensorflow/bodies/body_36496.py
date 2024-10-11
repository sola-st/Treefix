# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = variables.Variable(2.)
c = constant_op.constant(2.)

@def_function.function
def Fn():

    def Body1(v):
        x.assign(x)
        exit(v * x)

    ret1 = while_loop_v2(
        lambda v: v < 4.,
        Body1, [c],
        return_same_structure=False,
        name="while_1")  # 2x

    def Body2(v):
        x.assign(x)
        exit(v * x * x)

    ret2 = while_loop_v2(
        lambda v: v < 16.,
        Body2, [c],
        return_same_structure=False,
        name="while_2")  # 4x
    exit((ret1, ret2))

concrete_fn = Fn.get_concrete_function()
while_1 = concrete_fn.graph.get_operation_by_name("while_1")
while_2 = concrete_fn.graph.get_operation_by_name("while_2")
self.assertEqual(while_1.type, "While")
self.assertEqual(while_2.type, "While")
self.assertEmpty(while_1.control_inputs)
self.assertLen(while_2.control_inputs, 1)
self.assertIs(while_2.control_inputs[0], while_1)
