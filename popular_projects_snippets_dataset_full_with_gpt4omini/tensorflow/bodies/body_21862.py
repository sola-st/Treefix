# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
# Runtime check for empty string list.  This is slightly oblique:
# The queue runner should die with an assertion error on the null
# input tensor, causing the dequeue to fail with an OutOfRangeError.
with ops.Graph().as_default(), self.cached_session():
    coord = coordinator.Coordinator()
    queue = inp.string_input_producer(
        constant_op.constant(
            [], dtype=dtypes.string))
    dequeue = queue.dequeue()
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    threads = queue_runner_impl.start_queue_runners(coord=coord)
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(dequeue)
    coord.request_stop()
    for thread in threads:
        thread.join()
