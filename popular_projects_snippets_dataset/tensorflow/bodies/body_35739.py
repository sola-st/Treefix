# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
"""This test shows a very simple line model with test_loss.

    The template is used to share parameters between a training and test model.
    """
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

train_prediction = line_template(training_input)
test_prediction = line_template(test_input)

train_loss = math_ops.reduce_mean(
    math_ops.square(train_prediction - training_output))
test_loss = math_ops.reduce_mean(
    math_ops.square(test_prediction - test_output))

optimizer = gradient_descent.GradientDescentOptimizer(0.1)
train_op = optimizer.minimize(train_loss)

with session.Session() as sess:
    self.evaluate(variables.global_variables_initializer())
    initial_test_loss = self.evaluate(test_loss)
    self.evaluate(train_op)
    final_test_loss = self.evaluate(test_loss)

# Parameters are tied, so the loss should have gone down when we trained it.
self.assertLess(final_test_loss, initial_test_loss)
