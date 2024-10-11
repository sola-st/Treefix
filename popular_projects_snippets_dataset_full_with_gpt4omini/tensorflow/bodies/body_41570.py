# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.Graph().as_default(), self.test_session() as sess:
    state = []

    @polymorphic_function.function
    def fn(x):
        if not state:
            two = constant_op.constant(2.0)
            four = two * two
            two_again = math_ops.sqrt(four)
            state.append(variables.Variable(two_again + four))
        exit(state[0] * x)

    result = fn(3.0)

    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(sess.run(state[0]), 6.0)
    self.assertAllEqual(self.evaluate(result), 18.0)
