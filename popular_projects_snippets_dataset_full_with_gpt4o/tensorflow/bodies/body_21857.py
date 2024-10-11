# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    # Disable shape inference for the input.
    input_value = [[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]]
    input_tensor = array_ops.placeholder_with_default(input_value, shape=None)
    num_epochs = 2
    queue = inp.input_producer(
        input_tensor, element_shape=[4], num_epochs=num_epochs, shuffle=False)
    dequeue_many = queue.dequeue_many(len(input_value) * num_epochs)
    dequeue = queue.dequeue()
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners()

    # No randomness, so just see repeated copies of the input.
    self.assertAllEqual(input_value * num_epochs, self.evaluate(dequeue_many))

    # Reached the limit.
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(dequeue)
    for thread in threads:
        thread.join()
