# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    batch_size = 10
    num_batches = 3
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    examples = variables.Variable(zero64)
    counter = examples.count_up_to(num_batches * batch_size)
    string = array_ops.tile(["string"],
                            math_ops.cast(array_ops.stack([counter]),
                                          dtypes.int32))
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    batched = inp.batch(
        [counter, string], batch_size=batch_size, dynamic_pad=True)
    threads = queue_runner_impl.start_queue_runners()

    for i in range(num_batches):
        results = self.evaluate(batched)
        expected_results = np.arange(i * batch_size, (i + 1) * batch_size)
        max_len = expected_results[-1]
        self.assertAllEqual(results[0], expected_results)
        expected_strings = [[b"string"] * rep + [b""] * (max_len - rep)
                            for rep in expected_results]
        self.assertAllEqual(results[1], expected_strings)

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(batched)
    for thread in threads:
        thread.join()
