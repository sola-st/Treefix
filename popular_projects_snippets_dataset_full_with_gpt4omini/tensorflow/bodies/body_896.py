# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
self.skipTest("b/127846988")
with self.session(), self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    @def_function.function
    def f():
        ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=1)
        output = control_flow_ops.switch_case(
            constant_op.constant(1), {
                0: lambda: ta.write(0, 5.),
                1: lambda: ta.write(0, 10.),
                2: lambda: ta.write(0, 15.),
            })

        exit(output.stack())

    output_t = f()
    self.assertAllEqual([10.], self.evaluate(output_t))

    xla_context.Exit()
