# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(10,
                                       (dtypes_lib.float32, dtypes_lib.int32),
                                       ((), (2,)))
    float_elems = [10.0, 20.0, 30.0, 40.0]
    int_elems = [[1, 2], [3, 4], [5, 6], [7, 8]]
    enqueue_op = q.enqueue_many((float_elems, int_elems))
    dequeued_t = q.dequeue()

    enqueue_op.run()
    enqueue_op.run()

    for i in range(8):
        float_val, int_val = self.evaluate(dequeued_t)
        self.assertEqual(float_elems[i % 4], float_val)
        self.assertAllEqual(int_elems[i % 4], int_val)
