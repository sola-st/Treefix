# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    num_epochs = 1200
    source_strings = ["A", "B", "D", "G"]
    source_ints = [7, 3, 5, 2]
    slices = inp.slice_input_producer(
        [source_strings, source_ints],
        num_epochs=num_epochs,
        shuffle=True,
        seed=161803)
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    # Validate that we only shuffle the integers within an epoch and
    # count how often each possible order appears.
    expected = [
        b",".join(x)
        for x in itertools.permutations([b"A7", b"B3", b"D5", b"G2"])
    ]
    frequency = {}
    for e in expected:
        frequency[e] = 0
    for _ in range(num_epochs):
        output = [self.evaluate(slices) for _ in range(len(source_strings))]
        key = b",".join(s + compat.as_bytes(str(i)) for s, i in output)
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
        self.evaluate(slices)
    for thread in threads:
        thread.join()
