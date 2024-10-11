# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default():
    values = constant_op.constant([0, 1, 2, 3, 4, 5], dtype=dtypes.uint64)
    batched = inp.batch([values], batch_size=2)
    with self.cached_session() as sess:
        coord = coordinator.Coordinator()
        threads = queue_runner_impl.start_queue_runners(sess=sess, coord=coord)
        self.evaluate(batched)
        coord.request_stop()
        for thread in threads:
            thread.join()
