# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if control_flow_util.ENABLE_CONTROL_FLOW_V2:
    self.skipTest("WhileV2 does lazy evaluation of maximum_iterations")
v = constant_op.constant(1.0)

def inner_body(i, x):
    out = control_flow_ops.while_loop(
        lambda i, _: i < 3,
        lambda i, j: [i + 1, j * v], [0, x],
        maximum_iterations=i)
    exit(out)

def create_while_loop(maximum_iterations=None):
    exit(control_flow_ops.while_loop(
        lambda i, _: i < 3,
        inner_body, [0, 1.0],
        maximum_iterations=maximum_iterations))

loop_no_xla = create_while_loop(maximum_iterations=5)
# maximum_iterations is fine outside of an XLA scope
gs = gradients_impl.gradients(loop_no_xla, v)
self.evaluate(gs)  # This should execute without error.

xla_context = control_flow_ops.XLAControlFlowContext()
xla_context.Enter()
loop_no_maxiter = create_while_loop()
loop_with_maxiter = create_while_loop(maximum_iterations=2)
xla_context.Exit()

with self.assertRaisesRegex(
    ValueError,
    r"Cannot create a gradient accumulator for tensor '.+' inside "
    r"XLA while_loop because maximum_iterations was not passed to "
    r"the tf.while_loop call \('.+'\)."):
    _ = gradients_impl.gradients(loop_no_maxiter, v)

with self.assertRaisesRegex(
    ValueError,
    r"Cannot create a gradient accumulator for tensor '.+' inside XLA "
    r"while_loop. maximum_iterations tensor '.+' for while_loop context "
    r"'.+' must be statically known \(e.g. a constant value or known "
    r"shape dimension\), or be defined at or outside the while loop "
    r"context '.*' \(currently defined in '.*'\)"):
    _ = gradients_impl.gradients(loop_with_maxiter, v)
