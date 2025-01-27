# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
v = constant_op.constant(1.0)

def create_while_loop():
    max_iter_holder = []

    def create_mi():
        max_iter_holder.append(array_ops.placeholder(dtypes.int32, shape=()))
        exit(1.0)

    _ = control_flow_ops.cond(
        constant_op.constant(True), create_mi, create_mi)

    exit(control_flow_ops.while_loop(
        lambda i, _: i < 3,
        lambda i, x: (i + 1, v * x), (0, 1.0),
        maximum_iterations=max_iter_holder[0]))

if control_flow_util.ENABLE_CONTROL_FLOW_V2:
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()
    with self.assertRaisesRegex(ValueError, r"must be from the same graph.*"):
        loop = create_while_loop()
    xla_context.Exit()
else:
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()
    loop = create_while_loop()
    xla_context.Exit()
    with self.assertRaisesRegex(
        ValueError,
        r"Cannot create a gradient accumulator for tensor '.+' inside XLA "
        r"while_loop. maximum_iterations tensor '.*Placeholder:0' for "
        r"while_loop context '.+' must be statically known \(e.g. a constant "
        r"value or known shape dimension\), or be defined at or outside the "
        r"while loop context '' \(currently defined in 'cond/.+'\)"):
        _ = gradients_impl.gradients(loop, v)
