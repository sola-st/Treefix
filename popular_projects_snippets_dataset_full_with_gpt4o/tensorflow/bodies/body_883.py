# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
with self.session() as sess, self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    x = array_ops.placeholder(dtypes.float32)
    p = array_ops.placeholder(dtypes.int32)

    # TODO(b/129021699): Wrapping this in a tf.function does not work.
    def if_true():
        # This emits a StridedSlice op which expects the index to be a
        # compile-time const.
        exit(x[p])

    def if_false():
        exit(5.)

    output = control_flow_ops.cond(
        constant_op.constant(True), if_true, if_false)

    self.assertAllEqual(1.,
                        sess.run(output, feed_dict={
                            x: [0., 1., 2.],
                            p: 1
                        }))

    xla_context.Exit()
