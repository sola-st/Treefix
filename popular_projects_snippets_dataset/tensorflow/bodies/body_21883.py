# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    batch_size = 10
    num_batches = 3
    extra_elements = 5
    zero64 = constant_op.constant(0, dtype=dtypes.int64)

    examples = variables.Variable(zero64)
    counter = examples.count_up_to(num_batches * batch_size + extra_elements)
    sparse_counter = sparse_tensor.SparseTensor(
        indices=array_ops.reshape(zero64, [1, 1]),
        values=array_ops.stack([math_ops.cast(counter, dtypes.float32)]),
        dense_shape=[1])
    batched = inp.batch(
        [counter, sparse_counter, "string"],
        batch_size=batch_size,
        num_threads=4,
        allow_smaller_final_batch=True)
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    all_counts = []
    for i in range(num_batches):
        results = self.evaluate(batched)
        tf_logging.info("Batch %d: %s", i, results[0])
        self.assertEqual(len(results[0]), batch_size)
        self.assertAllEqual(results[0], results[1].values)
        self.assertAllEqual(
            results[1].indices,
            np.vstack((np.arange(batch_size), np.zeros(batch_size))).T)
        self.assertAllEqual(results[1].dense_shape, [batch_size, 1])
        all_counts.extend(results[0])
        self.assertAllEqual(results[2], [b"string"] * batch_size)

    # Reached the final batch with extra_elements.
    results = self.evaluate(batched)
    tf_logging.info("Last Batch: %s", results[0])
    self.assertEqual(len(results[0]), extra_elements)
    self.assertAllEqual(results[0], results[1].values)
    self.assertAllEqual(
        results[1].indices,
        np.vstack((np.arange(extra_elements), np.zeros(extra_elements))).T)
    self.assertAllEqual(results[1].dense_shape, [extra_elements, 1])
    all_counts.extend(results[0])
    self.assertAllEqual(results[2], [b"string"] * extra_elements)
    self.assertItemsEqual(all_counts,
                          range(num_batches * batch_size + extra_elements))

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched)
    for thread in threads:
        thread.join()
