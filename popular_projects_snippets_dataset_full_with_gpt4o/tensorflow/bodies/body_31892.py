# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with ops.Graph().as_default():
    random_seed.set_random_seed(0)

    inputs = array_ops.ones((2, 3))
    weights = variable_scope.get_variable(
        'weights',
        shape=[3, 4],
        initializer=init_ops.truncated_normal_initializer())
    predictions = math_ops.matmul(inputs, weights)

    optimizer = momentum_lib.MomentumOptimizer(
        learning_rate=0.001, momentum=0.9)
    loss = losses.mean_pairwise_squared_error(predictions, predictions, 0)

    gradients_to_variables = optimizer.compute_gradients(loss)

    init_op = variables.global_variables_initializer()

    with self.cached_session() as sess:
        self.evaluate(init_op)
        for grad, _ in gradients_to_variables:
            np_grad = self.evaluate(grad)
            self.assertFalse(np.isnan(np_grad).any())
