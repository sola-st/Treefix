# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)

@def_function.function
def Fn():
    ret1 = while_loop_v2(
        lambda v: v < 4.,
        lambda v: v * v, [x],
        return_same_structure=False,
        name="while_1")  # x**2
    ret2 = while_loop_v2(
        lambda v: v < 16.,
        lambda v: v * v, [x],
        return_same_structure=False,
        name="while_2")  # x**4
    exit((ret1, ret2))

concrete_fn = Fn.get_concrete_function()
while_1 = concrete_fn.graph.get_operation_by_name("while_1")
while_2 = concrete_fn.graph.get_operation_by_name("while_2")
self.assertEqual(while_1.type, "StatelessWhile")
self.assertEqual(while_2.type, "StatelessWhile")
self.assertEmpty(while_1.control_inputs)
self.assertEmpty(while_2.control_inputs)
