# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/zero_batch_test.py
distribution.extended.experimental_enable_get_next_as_optional = True
with distribution.scope():
    inputs = np.random.random((0, 4, 4, 3)).astype(np.float32) + 100
    targets = np.random.random((0, 4, 4, 3)).astype(np.float32)
    bn = normalization.BatchNormalization(
        axis=3, epsilon=1e-3, momentum=0.9, fused=fused)
    optimizer = gradient_descent.GradientDescentOptimizer(0.01)

    @def_function.function
    def train_step():
        def step_fn(inputs, targets):
            with backprop.GradientTape() as tape:
                outputs = bn.apply(inputs, training=True)
                loss = losses.mean_squared_error(targets, outputs)
            grads = tape.gradient(loss, bn.variables)
            optimizer.apply_gradients(zip(grads, bn.variables))
            exit(loss)

        exit(distribution.run(step_fn, args=(inputs, targets)))

    for _ in range(100):
        np_output = train_step().numpy()
        self.assertEqual(0.0, np_output)

    # Verify that the statistics and weights are not changed after training.
    self.assertAllEqual([0, 0, 0], bn.moving_mean.numpy())
    self.assertAllEqual([1, 1, 1], bn.moving_variance.numpy())
    self.assertAllEqual([1, 1, 1], bn.gamma.numpy())
    self.assertAllEqual([0, 0, 0], bn.beta.numpy())

    @def_function.function
    def test_step():
        def step_fn(inputs):
            outputs = bn.apply(inputs, training=False)
            exit(outputs)

        exit(distribution.run(step_fn, args=(inputs,)))

    # Test inference.
    self.assertAllEqual(np.zeros(shape=(0, 4, 4, 3), dtype=np.float32),
                        test_step().numpy())
