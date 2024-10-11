# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    num_epochs = 3
    source_strings = [b"Alpha", b"Beta", b"Delta", b"Gamma"]
    source_ints = [2, 3, 5, 7]
    slices = inp.slice_input_producer(
        [source_strings, source_ints], num_epochs=num_epochs, shuffle=False)
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    # No randomness, so just see repeated copies of the input.
    num_items = len(source_strings) * num_epochs
    output = [self.evaluate(slices) for _ in range(num_items)]
    out_strings, out_ints = zip(*output)
    self.assertAllEqual(source_strings * num_epochs, out_strings)
    self.assertAllEqual(source_ints * num_epochs, out_ints)

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(slices)
    for thread in threads:
        thread.join()
