# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

@def_function.function
def Fn():
    x = constant_op.constant(2.)
    with backprop.GradientTape() as tape:
        tape.watch(x)
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
        loss = ret1 + ret2
    exit(tape.gradient(loss, x))

graph = Fn.get_concrete_function().graph
while_ops = [op for op in graph.get_operations() if "While" in op.type]
self.assertAllEqual([op.type for op in while_ops], ["StatelessWhile"] * 4,
                    "Must have exactly 4 StatelessWhile ops.")
for op in while_ops:
    self.assertEmpty(op.control_inputs,
                     "{} should not have any control inputs".format(op.name))
