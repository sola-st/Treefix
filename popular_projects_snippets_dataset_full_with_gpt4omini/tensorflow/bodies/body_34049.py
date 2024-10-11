# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    q1 = data_flow_ops.PaddingFIFOQueue(
        1, dtypes_lib.float32, ((),), shared_name="shared_queue")
    q1.enqueue((10.0,)).run()

    q2 = data_flow_ops.PaddingFIFOQueue(
        1, dtypes_lib.float32, ((),), shared_name="shared_queue")

    q1_size_t = q1.size()
    q2_size_t = q2.size()

    self.assertEqual(self.evaluate(q1_size_t), [1])
    self.assertEqual(self.evaluate(q2_size_t), [1])

    self.assertEqual(q2.dequeue().eval(), [10.0])

    self.assertEqual(self.evaluate(q1_size_t), [0])
    self.assertEqual(self.evaluate(q2_size_t), [0])

    q2.enqueue((20.0,)).run()

    self.assertEqual(self.evaluate(q1_size_t), [1])
    self.assertEqual(self.evaluate(q2_size_t), [1])

    self.assertEqual(q1.dequeue().eval(), [20.0])

    self.assertEqual(self.evaluate(q1_size_t), [0])
    self.assertEqual(self.evaluate(q2_size_t), [0])
