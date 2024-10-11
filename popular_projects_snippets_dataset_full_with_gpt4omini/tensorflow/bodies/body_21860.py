# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    strings = [b"a", b"b", b"c"]
    num_epochs = 600
    queue = inp.string_input_producer(
        strings, num_epochs=num_epochs, shuffle=True, seed=271828)
    dequeue_many = queue.dequeue_many(len(strings))
    dequeue = queue.dequeue()
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    # Validate that we only shuffle the strings within an epoch and
    # count how often each possible order appears.
    expected = [b"abc", b"acb", b"bac", b"bca", b"cab", b"cba"]
    frequency = {}
    for e in expected:
        frequency[e] = 0
    for _ in range(num_epochs):
        output = self.evaluate(dequeue_many)
        key = b"".join(output)
        self.assertIn(key, expected)
        frequency[key] += 1

    # Expect an approximately even distribution over all possible orders.
    expected_frequency = num_epochs / len(expected)
    margin = expected_frequency * 0.4
    tf_logging.info("Observed counts: %s", frequency)
    for key in expected:
        value = frequency[key]
        self.assertGreater(value, expected_frequency - margin)
        self.assertLess(value, expected_frequency + margin)

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(dequeue)
    for thread in threads:
        thread.join()
