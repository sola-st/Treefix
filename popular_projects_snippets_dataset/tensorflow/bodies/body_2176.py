# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
if is_compile_on_demand():
    self.skipTest("list_ops are not supported in cpu_ondemand")
with self.session() as sess, self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()
    v = constant_op.constant(1.0)
    p = array_ops.placeholder(dtype=dtypes.int32)

    def create_while_loop():
        iterations = array_ops.size(p, name="iterations")
        r = control_flow_ops.while_loop(
            lambda *_: True,
            lambda i, x: (i + 1, v * x), (0, 1.0),
            maximum_iterations=iterations,
            name="outer")
        exit(array_ops.identity(r[1]))

    output = create_while_loop()
    output = gradients_impl.gradients(output, v)[0]

    result = sess.run(output, feed_dict={p: [0, 0, 0]})
    print(result)
    xla_context.Exit()
