# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with self.cached_session() as sess:
    with session.Session() as other_sess:
        zero64 = constant_op.constant(0, dtype=dtypes.int64)
        var = variables.VariableV1(zero64)
        count_up_to = var.count_up_to(3)
        queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
        self.evaluate(variables.global_variables_initializer())
        coord = coordinator.Coordinator()
        qr = queue_runner_impl.QueueRunner(queue, [count_up_to])
        # NOTE that this test does not actually start the threads.
        threads = qr.create_threads(sess, coord=coord)
        other_threads = qr.create_threads(other_sess, coord=coord)
        self.assertEqual(len(threads), len(other_threads))
