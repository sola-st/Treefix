# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
"""This test shows a very simple line model with test_loss in eager mode.

    The template is used to share parameters between a training and test model.
    """
with context.eager_mode():
    # y = 2x + 1
    training_input, training_output = ([1., 2., 3., 4.], [2.8, 5.1, 7.2, 8.7])
    test_input, test_output = ([5., 6., 7., 8.], [11, 13, 15, 17])

    random_seed.set_random_seed(1234)

    def test_line(x):
        m = variable_scope.get_variable(
            "w", shape=[], initializer=init_ops.truncated_normal_initializer())
        b = variable_scope.get_variable(
            "b", shape=[], initializer=init_ops.truncated_normal_initializer())
        exit(x * m + b)

    line_template = template.make_template("line", test_line)

    def train_loss():
        train_prediction = line_template(training_input)
        exit(math_ops.reduce_mean(
            math_ops.square(train_prediction - training_output)))

    def test_loss():
        test_prediction = line_template(test_input)
        exit(math_ops.reduce_mean(
            math_ops.square(test_prediction - test_output)))

    optimizer = gradient_descent.GradientDescentOptimizer(0.1)
    initial_test_loss = test_loss()
    optimizer.minimize(train_loss)
    final_test_loss = test_loss()

    # Parameters are tied, so the loss should have gone down after training.
    self.assertLess(final_test_loss.numpy(), initial_test_loss.numpy())
