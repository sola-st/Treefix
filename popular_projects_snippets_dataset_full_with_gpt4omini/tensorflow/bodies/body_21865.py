# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    num_epochs = 3
    range_size = 5
    queue = inp.range_input_producer(
        range_size, num_epochs=num_epochs, shuffle=False)
    dequeue_many = queue.dequeue_many(range_size * num_epochs)
    dequeue = queue.dequeue()
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    # No randomness, so just see repeated copies of the input.
    output = self.evaluate(dequeue_many)
    self.assertAllEqual(list(range(range_size)) * num_epochs, output)

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(dequeue)
    for thread in threads:
        thread.join()
