# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
g = ops.Graph()
with session.Session(graph=g), g.as_default(), self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    @def_function.function
    def f():
        ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=1)
        output = control_flow_ops.cond(
            constant_op.constant(False),
            lambda: ta.write(0, 5.), lambda: ta.write(0, 10.))

        exit(output.stack())

    output_t = f()
    self.assertAllEqual([10.], self.evaluate(output_t))

    xla_context.Exit()
