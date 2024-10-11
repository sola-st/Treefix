# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    strings = [b"to", b"be", b"or", b"not", b"to", b"be"]
    queue = inp.string_input_producer(strings, shuffle=False)
    coord = coordinator.Coordinator()
    threads = queue_runner_impl.start_queue_runners(sess=sess, coord=coord)
    for _ in range(2):
        for string in strings:
            # NOTE(mrry): This is not the recommended way to write
            # dequeuing code (instead you should create a single dequeue
            # op before starting the queue runners, and run it
            # repeatedly), because it leads to concurrent reading and
            # writing of the `tf.Graph` object. However, many users
            # write code this way, so we include this test to ensure
            # that we can support it.
            self.assertEqual(string, self.evaluate(queue.dequeue()))
    coord.request_stop()
    coord.join(threads)
