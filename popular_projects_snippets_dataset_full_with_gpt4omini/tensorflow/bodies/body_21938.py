# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    batch_size = 5
    num_batches = 4
    examples = variables.Variable(0)
    counter = examples.count_up_to(num_batches * batch_size * 2)
    sparse_counter = sparse_tensor.SparseTensor(
        indices=array_ops.zeros(
            [1, 1], dtype=dtypes.int64),
        values=array_ops.stack([math_ops.cast(counter, dtypes.float32)]),
        dense_shape=[1])
    to_batch = [counter, sparse_counter, "string"]
    if enqueue_many:
        to_batch = inp.batch(to_batch, 4 if keep_input_vector else 1)
    keep_input = array_ops.squeeze(
        math_ops.equal(0, math_ops.mod(to_batch[0], 2)))
    batched = inp.maybe_shuffle_batch(
        to_batch,
        batch_size,
        10,
        1,
        keep_input,
        num_threads=num_threads,
        enqueue_many=enqueue_many)
    variables.initialize_all_variables().run()
    variables.initialize_local_variables().run()
    threads = queue_runner_impl.start_queue_runners()

    for _ in range(num_batches):
        results = self.evaluate(batched)
        self.assertAllEqual([0] * batch_size, np.mod(results[0], 2))
        self.assertAllEqual([0] * batch_size, np.mod(results[1].values, 2))
        self.assertAllEqual([b"string"] * batch_size, results[2])

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched)
    for thread in threads:
        thread.join()
