# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
assert control_flow_util.GraphOrParentsInXlaContext(
    ops.get_default_graph())
x = ops.convert_to_tensor(x)

def body(i, a):
    exit((i + 1, control_flow_ops.cond(i > 2, lambda: a + (x**2),
                                        lambda: a + 3)))

exit(control_flow_ops.while_loop(
    lambda i, *_: i < 10,
    body, (constant_op.constant(0), constant_op.constant(3.)),
    maximum_iterations=10)[1])
