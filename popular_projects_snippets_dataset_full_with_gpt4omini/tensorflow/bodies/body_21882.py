# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    batch_size = 10
    num_batches = 3
    extra_elements = 5
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    examples = variables.Variable(zero64)
    counter = examples.count_up_to(num_batches * batch_size + extra_elements)
    sparse_counter = sparse_tensor.SparseTensor(
        indices=array_ops.reshape(
            array_ops.stack([zero64, zero64 + 1]), [2, 1]),
        values=math_ops.cast(
            array_ops.stack([counter, -counter]), dtypes.float32),
        dense_shape=[2])
    batched = inp.batch(
        [counter, sparse_counter, "string"],
        batch_size=batch_size,
        allow_smaller_final_batch=True)
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    for i in range(num_batches):
        results = self.evaluate(batched)
        self.assertAllEqual(results[0],
                            np.arange(i * batch_size, (i + 1) * batch_size))
        self.assertAllEqual(
            results[1].indices,
            np.vstack((
                np.arange(2 * batch_size) // 2,  # 0, 0, 1, 1, ...
                [0, 1] * batch_size)).T)
        #  [x, -x, x+1, -(x+1), ...]
        expected = np.arange(2 * i * batch_size, 2 * (i + 1) * batch_size) // 2
        expected *= ([1, -1] * batch_size)  # mult by [1, -1, 1, -1, ...]
        self.assertAllEqual(results[1].values, expected)
        self.assertAllEqual(results[1].dense_shape, [batch_size, 2])
        self.assertAllEqual(results[2], [b"string"] * batch_size)

    # Reached the final batch with extra_elements.
    results = self.evaluate(batched)
    self.assertAllEqual(results[0],
                        np.arange(num_batches * batch_size,
                                  num_batches * batch_size + extra_elements))
    self.assertAllEqual(
        results[1].indices,
        np.vstack((
            np.arange(2 * extra_elements) // 2,  # 0, 0, 1, 1, ...
            [0, 1] * extra_elements)).T)
    self.assertAllEqual(results[1].dense_shape, [extra_elements, 2])
    self.assertAllEqual(results[2], [b"string"] * extra_elements)

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched)
    for thread in threads:
        thread.join()
