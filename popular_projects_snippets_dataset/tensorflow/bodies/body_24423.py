# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    q = data_flow_ops.FIFOQueue(3, "float", name="fifo_queue")
    q_init = q.enqueue_many(([101.0, 202.0, 303.0],), name="enqueue_many")

    _, dump = self._debug_run_and_get_dump(sess, q_init)
    self.assertTrue(dump.loaded_partition_graphs())

    fifo_queue_tensor = dump.get_tensors("fifo_queue", 0, "DebugIdentity")[0]
    self.assertIsInstance(fifo_queue_tensor,
                          debug_data.InconvertibleTensorProto)
    self.assertTrue(fifo_queue_tensor.initialized)
    self.assertAllClose(
        [101.0, 202.0, 303.0],
        dump.get_tensors("enqueue_many/component_0", 0, "DebugIdentity")[0])
