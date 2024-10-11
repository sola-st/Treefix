# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
with self.session() as sess, self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()

    x = array_ops.placeholder(dtypes.float32)
    p = random_ops.random_uniform([], minval=1, maxval=3, dtype=dtypes.int32)
    condition = math_ops.cast(
        random_ops.random_uniform([], minval=0, maxval=2, dtype=dtypes.int32),
        dtypes.bool)

    def f():
        # TODO(b/129021699): Wrapping this in a tf.function does not work.
        def if_true():
            # This emits a StridedSlice op which expects the index to be a
            # compile-time const.
            exit(x[:p])

        def if_false():
            exit(array_ops.fill([p], 5.))

        exit(control_flow_ops.cond(condition, if_true, if_false))

    output = xla.compile(f)

    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "must be a compile-time constant"):
        sess.run(
            output, feed_dict={
                x: [0., 1., 2.],
            })

    xla_context.Exit()
