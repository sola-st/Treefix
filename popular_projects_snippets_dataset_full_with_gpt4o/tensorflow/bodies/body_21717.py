# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
# CountUpTo will raise OUT_OF_RANGE when it reaches the count.
zero64 = constant_op.constant(0, dtype=dtypes.int64)
var = variables.VariableV1(zero64)
count_up_to = var.count_up_to(3)
queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
init_op = variables.global_variables_initializer()
qr = queue_runner_impl.QueueRunner(queue, [count_up_to])
queue_runner_impl.add_queue_runner(qr)
with self.cached_session() as sess:
    init_op.run()
    threads = queue_runner_impl.start_queue_runners(sess)
    for t in threads:
        t.join()
    self.assertEqual(0, len(qr.exceptions_raised))
    # The variable should be 3.
    self.assertEqual(3, self.evaluate(var))
