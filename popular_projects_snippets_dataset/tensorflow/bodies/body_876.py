# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
# TODO(b/132430685): Make test more useful. Also b/129396295, b/127846988
with self.session(), self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    @def_function.function
    def f():
        ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=1)
        output = control_flow_ops.cond(
            constant_op.constant(True),
            lambda: ta.write(0, 5.), lambda: ta.write(0, 10.))

        exit(output.stack())

    output_t = f()
    self.assertAllEqual([5.], self.evaluate(output_t))

    xla_context.Exit()
