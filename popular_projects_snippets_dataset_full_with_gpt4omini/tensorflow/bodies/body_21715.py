# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with self.cached_session() as sess:
    # CountUpTo will raise OUT_OF_RANGE when it reaches the count.
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    var = variables.VariableV1(zero64)
    count_up_to = var.count_up_to(3)
    queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
    self.evaluate(variables.global_variables_initializer())
    qr = queue_runner_impl.QueueRunner(queue, [count_up_to,
                                               _MockOp("bad_op")])
    threads = qr.create_threads(sess, start=True)
    self.assertEqual(sorted(t.name for t in threads),
                     ["QueueRunnerThread-fifo_queue-CountUpTo:0",
                      "QueueRunnerThread-fifo_queue-bad_op"])
    for t in threads:
        t.join()
    exceptions = qr.exceptions_raised
    self.assertEqual(1, len(exceptions))
    self.assertTrue("Operation not in the graph" in str(exceptions[0]))

    threads = qr.create_threads(sess, start=True)
    for t in threads:
        t.join()
    exceptions = qr.exceptions_raised
    self.assertEqual(1, len(exceptions))
    self.assertTrue("Operation not in the graph" in str(exceptions[0]))
