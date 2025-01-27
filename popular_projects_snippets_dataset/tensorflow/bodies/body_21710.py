# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with self.cached_session() as sess:
    # CountUpTo will raise OUT_OF_RANGE when it reaches the count.
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    var = variables.VariableV1(zero64)
    count_up_to = var.count_up_to(3)
    queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
    self.evaluate(variables.global_variables_initializer())
    qr = queue_runner_impl.QueueRunner(queue, [count_up_to])
    # As the coordinator to stop.  The queue runner should
    # finish immediately.
    coord = coordinator.Coordinator()
    coord.request_stop()
    threads = qr.create_threads(sess, coord)
    self.assertEqual(sorted(t.name for t in threads),
                     ["QueueRunnerThread-fifo_queue-CountUpTo:0",
                      "QueueRunnerThread-fifo_queue-close_on_stop"])
    for t in threads:
        t.start()
    coord.join()
    self.assertEqual(0, len(qr.exceptions_raised))
    # The variable should be 0.
    self.assertEqual(0, self.evaluate(var))
