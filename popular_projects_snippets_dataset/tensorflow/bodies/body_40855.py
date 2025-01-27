# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    def fn(x, a):
        exit(2 * x + a)

    xla_func = polymorphic_function.function(fn, jit_compile=True)

    with backprop.GradientTape() as tape:
        inputs = constant_op.constant([1., 2., 2., 3., 3.])
        tape.watch(inputs)
        outputs = xla_func(inputs, 1)

    self.assertAllClose([2, 2, 2, 2, 2], tape.gradient(outputs, inputs))

    # pylint: disable=protected-access
    (forward, backward) = xla_func.get_concrete_function(
        inputs, 1)._delayed_rewrite_functions.forward_backward()

    # Check that the must-compile attribute gets correctly propagated to the
    # created derivatives.
    self.assertTrue(backward.function_def.attr['_XlaMustCompile'])
    self.assertTrue(forward.definition.attr['_XlaMustCompile'])
