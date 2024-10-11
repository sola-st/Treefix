# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
np.random.seed(42)
for num_inputs in range(1, 10):
    with test_util.use_gpu():
        input_vars = [
            variables.Variable(10.0 * np.random.random())
            for _ in range(0, num_inputs)
        ]
        self.evaluate(variables.global_variables_initializer())
        if context.executing_eagerly():
            with backprop.GradientTape() as tape:
                tape.watch(input_vars)
                addn = math_ops.add_n(input_vars)
                add_n_grad = tape.gradient(addn, input_vars)
        else:
            addn = math_ops.add_n(input_vars)
            add_n_grad = gradients.gradients(addn, input_vars)

        self.assertAllEqual(
            np.repeat(1.0, num_inputs),  # d/dx (x + y + ...) = 1
            [self.evaluate(g) for g in add_n_grad])
