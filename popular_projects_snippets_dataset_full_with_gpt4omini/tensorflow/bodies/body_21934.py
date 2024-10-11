# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    batch_size = 10
    num_batches = 3
    extra_elements = 5
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    examples = variables.Variable(zero64)
    total_elements = num_batches * batch_size + extra_elements
    counter = examples.count_up_to(total_elements)
    sparse_counter = sparse_tensor.SparseTensor(
        indices=array_ops.reshape(zero64, [1, 1]),
        values=array_ops.stack([math_ops.cast(counter, dtypes.float32)]),
        dense_shape=[1])
    batched = inp.shuffle_batch(
        [counter, sparse_counter, "string"],
        batch_size=batch_size,
        capacity=32,
        min_after_dequeue=16,
        seed=141421,
        allow_smaller_final_batch=True)
    batched_fetch = batched
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    all_counts = []
    for _ in range(num_batches):
        results = self.evaluate(batched_fetch)
        self.assertEqual(len(results[0]), batch_size)
        all_counts.extend(results[0])
        self.assertAllEqual(
            results[1].indices,
            np.vstack((np.arange(batch_size), np.zeros(batch_size))).T)
        self.assertAllEqual(results[0], results[1].values)
        self.assertAllEqual(results[1].dense_shape, [batch_size, 1])
        self.assertAllEqual(results[2], [b"string"] * batch_size)

    # Reached the final batch with extra elements.
    results = self.evaluate(batched)
    self.assertAllEqual(results[1].dense_shape, [extra_elements, 1])
    self.assertAllEqual(results[2], [b"string"] * extra_elements)
    all_counts.extend(results[0])

    # Results scrambled, but include all the expected numbers.
    deltas = [
        all_counts[i + 1] - all_counts[i] for i in range(len(all_counts) - 1)
    ]
    self.assertFalse(all(d == deltas[0] for d in deltas))
    self.assertItemsEqual(all_counts, range(total_elements))

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched_fetch)
    for thread in threads:
        thread.join()
