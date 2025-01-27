# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/zero_batch_test.py
distribution.extended.experimental_enable_get_next_as_optional = True
with distribution.scope(), self.cached_session() as sess:
    bn_list = []
    inputs = np.random.random((0, 4, 4, 3)) + 100
    targets = np.random.random((0, 4, 4, 3))
    inputs_placeholder = array_ops.placeholder(
        dtype=dtypes.float32, shape=[None, 4, 4, 3])
    targets_placeholder = array_ops.placeholder(
        dtype=dtypes.float32, shape=[None, 4, 4, 3])

    def step_fn(is_training, inputs, targets=None):
        bn = normalization.BatchNormalization(
            axis=3, epsilon=1e-3, momentum=0.9, fused=fused)
        bn_list.append(bn)
        outputs = bn.apply(inputs, training=is_training)
        if not is_training:
            exit(outputs)

        loss = losses.mean_squared_error(targets, outputs)
        optimizer = gradient_descent.GradientDescentOptimizer(0.01)
        train_op = optimizer.minimize(loss)
        with ops.control_dependencies([train_op]):
            exit(array_ops.identity(loss))

    train_op = distribution.extended.call_for_each_replica(
        step_fn, args=(True, inputs_placeholder, targets_placeholder))
    predict_op = distribution.extended.call_for_each_replica(
        step_fn, args=(False, inputs_placeholder))
    bn = bn_list[0]

    self.evaluate(variables.global_variables_initializer())

    # Check for initial statistics and weights.
    moving_mean, moving_var = self.evaluate(
        [bn.moving_mean, bn.moving_variance])
    self.assertAllEqual([0, 0, 0], moving_mean)
    self.assertAllEqual([1, 1, 1], moving_var)

    np_gamma, np_beta = self.evaluate([bn.gamma, bn.beta])
    self.assertAllEqual([1, 1, 1], np_gamma)
    self.assertAllEqual([0, 0, 0], np_beta)

    for _ in range(100):
        np_output, _, _ = sess.run([train_op] + bn.updates, {
            inputs_placeholder: inputs,
            targets_placeholder: targets
        })
        self.assertEqual(0.0, np_output)

    # Verify that the statistics and weights are not changed after training.
    moving_mean, moving_var = self.evaluate(
        [bn.moving_mean, bn.moving_variance])
    self.assertAllEqual([0, 0, 0], moving_mean)
    self.assertAllEqual([1, 1, 1], moving_var)

    np_gamma, np_beta = self.evaluate([bn.gamma, bn.beta])
    self.assertAllEqual([1, 1, 1], np_gamma)
    self.assertAllEqual([0, 0, 0], np_beta)

    # Test inference.
    np_output = sess.run(predict_op, {inputs_placeholder: inputs})
    self.assertEqual([], np_output.tolist())
