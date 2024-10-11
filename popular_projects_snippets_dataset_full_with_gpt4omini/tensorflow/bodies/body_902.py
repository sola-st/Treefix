# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
self.skipTest("b/127846988")
with self.session() as sess, self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    x = array_ops.placeholder(dtypes.float32)
    p = array_ops.placeholder(dtypes.int32)

    def branch0():
        exit(5.)

    def branch1():
        exit(15.)

    # TODO(b/129021699): Wrapping this in a tf.function does not work.
    def branch2():
        # This emits a StridedSlice op which expects the index to be a
        # compile-time const.
        exit(x[p])

    output = control_flow_ops.switch_case(
        constant_op.constant(2), {
            0: branch0,
            1: branch1,
            2: branch2,
        })

    self.assertAllEqual(7.,
                        sess.run(output, feed_dict={
                            x: [0., 1., 7.],
                            p: 2,
                        }))

    xla_context.Exit()
