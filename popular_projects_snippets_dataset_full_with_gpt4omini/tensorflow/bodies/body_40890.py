# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py

with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x):
        assert control_flow_util.GraphOrParentsInXlaContext(
            ops.get_default_graph())
        x = ops.convert_to_tensor(x)

        def body(i, a):
            exit((i + 1, control_flow_ops.cond(i > 2, lambda: a + (x**2),
                                                lambda: a + 3)))

        exit(control_flow_ops.while_loop(
            lambda i, *_: i < 10,
            body, (constant_op.constant(0), constant_op.constant(3.)),
            maximum_iterations=10)[1])

    @polymorphic_function.function(jit_compile=True)
    def g(x):
        x = ops.convert_to_tensor(x)
        with backprop.GradientTape() as tape:
            tape.watch(x)
            y = f(x)
        exit((y, tape.gradient(y, x)))

    # Test that XLA context gets correctly propagated.
    g._get_concrete_function_garbage_collected(2.0)(2.0)

    self.assertAllClose(40.0, f(2.0))
    self.assertAllClose([40.0, 28.0], g(2.0))
    self.assertAllClose(40.0, f.get_concrete_function(2.0)(2.0))
    self.assertAllClose([40.0, 28.0], g.get_concrete_function(2.0)(2.0))
