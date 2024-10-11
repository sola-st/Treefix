# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    batch_size = 10
    num_batches = 3
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    examples = variables.Variable(zero64)
    counter = examples.count_up_to(num_batches * batch_size)
    sparse_counter = sparse_tensor.SparseTensor(
        indices=array_ops.reshape(zero64, [1, 1]),
        values=array_ops.stack([math_ops.cast(counter, dtypes.float32)]),
        dense_shape=[1])
    batched = inp.shuffle_batch(
        [counter, sparse_counter, "string"],
        batch_size=batch_size,
        capacity=32,
        min_after_dequeue=16,
        seed=173205,
        num_threads=4)
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    all_counts = []
    for i in range(num_batches):
        results = self.evaluate(batched)
        tf_logging.info("Batch %d: %s", i, results[0])
        self.assertEqual(len(results[0]), batch_size)
        all_counts.extend(results[0])
        self.assertAllEqual(
            results[1].indices,
            np.vstack((np.arange(batch_size), np.zeros(batch_size))).T)
        self.assertAllEqual(results[0], results[1].values)
        self.assertAllEqual(results[1].dense_shape, [batch_size, 1])
        self.assertAllEqual(results[2], [b"string"] * batch_size)
    # Results scrambled, but include all the expected numbers.
    deltas = [
        all_counts[i + 1] - all_counts[i] for i in range(len(all_counts) - 1)
    ]
    self.assertFalse(all(d == deltas[0] for d in deltas))
    self.assertItemsEqual(all_counts, range(num_batches * batch_size))

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched)
    for thread in threads:
        thread.join()
