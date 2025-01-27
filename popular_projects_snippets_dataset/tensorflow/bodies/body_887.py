# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
self.skipTest("b/132430685")
with self.session(), self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    x = array_ops.placeholder_with_default([0., 1., 2.], shape=[3])
    p = constant_op.constant(1)

    def f():
        # TODO(b/129021699): Wrapping this in a tf.function does not work.
        def if_true():
            # This emits a StridedSlice op which expects the index to be a
            # compile-time const.
            exit(x[p])

        def if_false():
            exit(5.)

        exit(control_flow_ops.cond(
            constant_op.constant(True), if_true, if_false))

    output = xla.compile(f)

    self.assertAllEqual(1., self.evaluate(output))

    xla_context.Exit()
