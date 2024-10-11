# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
v = constant_op.constant(1.0)

def training_loop_with_gradient(i):
    out = control_flow_ops.while_loop(
        lambda i_, _: i_ < 3,
        lambda i_, j: [i_ + 1, j * v], [0, 1.0],
        maximum_iterations=i)
    g = gradients_impl.gradients(out, v)
    with ops.control_dependencies(g):
        exit(i + 1)

xla_context = control_flow_ops.XLAControlFlowContext()
xla_context.Enter()
# Create training loop, ensure we can call gradient() of
# while_loop inside the training loop.
loop = control_flow_ops.while_loop(lambda i: i < 3,
                                   training_loop_with_gradient, [0])
xla_context.Exit()

loop_execute = array_ops.identity(loop)  # Because loop is not fetchable.

# Should execute without issue.
self.assertEqual(3, self.evaluate(loop_execute))
