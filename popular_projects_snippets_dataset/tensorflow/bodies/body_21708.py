# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with self.cached_session() as sess:
    queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
    qr = queue_runner_impl.QueueRunner(queue, [_MockOp("i fail"),
                                               _MockOp("so fail")])
    threads = qr.create_threads(sess)
    self.evaluate(variables.global_variables_initializer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    exceptions = qr.exceptions_raised
    self.assertEqual(2, len(exceptions))
    self.assertTrue("Operation not in the graph" in str(exceptions[0]))
    self.assertTrue("Operation not in the graph" in str(exceptions[1]))
