# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
with ops.name_scope("scope"):
    queue = data_flow_ops.FIFOQueue(10, dtypes.float32, name="queue")
qr = queue_runner_impl.QueueRunner(queue, [control_flow_ops.no_op()])
self.assertEqual("scope/queue", qr.name)
queue_runner_impl.add_queue_runner(qr)
self.assertEqual(
    1, len(ops.get_collection(ops.GraphKeys.QUEUE_RUNNERS, "scope")))
