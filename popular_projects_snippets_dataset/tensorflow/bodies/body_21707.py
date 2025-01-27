# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with self.cached_session() as sess:
    # CountUpTo will raise OUT_OF_RANGE when it reaches the count.
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    var0 = variables.VariableV1(zero64)
    count_up_to_3 = var0.count_up_to(3)
    var1 = variables.VariableV1(zero64)
    count_up_to_30 = var1.count_up_to(30)
    queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
    qr = queue_runner_impl.QueueRunner(queue, [count_up_to_3, count_up_to_30])
    threads = qr.create_threads(sess)
    self.assertEqual(sorted(t.name for t in threads),
                     ["QueueRunnerThread-fifo_queue-CountUpTo:0",
                      "QueueRunnerThread-fifo_queue-CountUpTo_1:0"])
    self.evaluate(variables.global_variables_initializer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    self.assertEqual(0, len(qr.exceptions_raised))
    self.assertEqual(3, self.evaluate(var0))
    self.assertEqual(30, self.evaluate(var1))
