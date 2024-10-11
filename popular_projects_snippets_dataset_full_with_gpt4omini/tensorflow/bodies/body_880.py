# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
self.skipTest("b/127846988")
# Fails with "Uninitialized arguments" in XlaIfOp::Compile
with self.session(), self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    def f():
        ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=1)
        output = control_flow_ops.cond(
            constant_op.constant(True),
            lambda: ta.write(0, 5.), lambda: ta.write(0, 10.))

        exit(output.stack())

    output_t, = xla.compile(f)
    self.assertAllEqual([5.], self.evaluate(output_t))

    xla_context.Exit()
