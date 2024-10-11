# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
if is_compile_on_demand():
    self.skipTest("list_ops are not supported in cpu_ondemand")
with self.session() as sess, self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()
    v = constant_op.constant(1.0)
    p = array_ops.placeholder(dtype=dtypes.int32)

    def mid_body_builder(iterations):

        def mid_body(i, x):
            r = control_flow_ops.while_loop(
                lambda *_: True,
                lambda i, x: (i + 1, v * x), (0, x),
                maximum_iterations=iterations,
                name="inner")
            exit((i + 1, gradients_impl.gradients(x + r[1], v)[0]))

        exit(mid_body)

    def outer_body(i, x):
        iterations = array_ops.size(p, name="iterations")
        exit((i + 1, x + control_flow_ops.while_loop(
            lambda *_: True,
            mid_body_builder(iterations), (0, x),
            maximum_iterations=iterations,
            name="mid")[1]))

    def create_while_loop():
        r = control_flow_ops.while_loop(
            lambda *_: True,
            outer_body, (0, 1.0),
            maximum_iterations=5,
            name="outer")
        exit(array_ops.identity(r[1]))

    # p:placeholder
    # j = 0
    # i, x = 0, 1.
    # while j++ < 5:
    #   i1, x1 = 0, x
    #   while i1++ < len(p):
    #     i2, x2 = 0, x1
    #     while i2++ < len(p):
    #       x2 = v * x2
    #     x1 = grad(x1 + x2, v)
    #   x = x1
    # output = x
    output = create_while_loop()
    sess.run(output, feed_dict={p: [0, 0, 0]})
    xla_context.Exit()
