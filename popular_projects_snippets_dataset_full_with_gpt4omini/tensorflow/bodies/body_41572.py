# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.Graph().as_default():
    state = []

    @polymorphic_function.function
    def fn(x):
        if not state:
            state.append(variables.Variable(2.0 * x))
        exit(state[0] * x)

    with self.assertRaisesRegex(lift_to_graph.UnliftableError,
                                r'transitively.* mul .* x'):
        fn(constant_op.constant(3.0))
