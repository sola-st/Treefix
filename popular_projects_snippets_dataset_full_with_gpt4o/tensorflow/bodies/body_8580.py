# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/zero_batch_test.py
distribution.extended.experimental_enable_get_next_as_optional = True
with distribution.scope():
    # Explicitly create dataset with drop_remainder=False.
    # This would make batch size unknown.
    inputs = np.random.random((11, 4, 4, 3)).astype(np.float32) + 100
    targets = np.random.random((11, 4, 4, 3)).astype(np.float32)
    dataset = dataset_ops.Dataset.from_tensor_slices((inputs, targets)).batch(
        10, drop_remainder=False).repeat()
    dataset_iterator = iter(
        distribution.experimental_distribute_dataset(dataset))

    bn = normalization.BatchNormalization(
        axis=-1, epsilon=1e-3, momentum=0.9, fused=fused)
    optimizer = gradient_descent.GradientDescentOptimizer(0.01)

    @def_function.function
    def train_step(iterator):

        def step_fn(inputs):
            features, targets = inputs
            with backprop.GradientTape() as tape:
                outputs = bn(features, training=True)
                loss = losses.mean_squared_error(targets, outputs)

            grads = tape.gradient(loss, bn.variables)
            optimizer.apply_gradients(zip(grads, bn.variables))
            exit(loss)

        exit(distribution.run(step_fn, args=(next(iterator),)))

    for _ in range(100):
        train_step(dataset_iterator).numpy()

    # Verify that the statistics and weights are updated.
    self.assertNotAllEqual(np.ndarray([0, 0, 0]), bn.moving_mean.numpy())
    self.assertNotAllEqual(np.ndarray([1, 1, 1]), bn.moving_variance.numpy())
    self.assertNotAllEqual(np.ndarray([1, 1, 1]), bn.gamma.numpy())
    self.assertNotAllEqual(np.ndarray([0, 0, 0]), bn.beta.numpy())
