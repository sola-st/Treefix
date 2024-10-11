# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(
    10, (dtypes_lib.float32, dtypes_lib.int32), shapes=((), (2,)))
float_elems = [
    10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0
]
int_elems = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14],
             [15, 16], [17, 18], [19, 20]]

self.evaluate(q.enqueue_many((float_elems, int_elems)))

dequeued_t = q.dequeue_many(4)
float_val, int_val = self.evaluate(dequeued_t)
self.assertAllEqual(float_elems[0:4], float_val)
self.assertAllEqual(int_elems[0:4], int_val)
self.assertEqual(float_val.shape, dequeued_t[0].get_shape())
self.assertEqual(int_val.shape, dequeued_t[1].get_shape())

float_val, int_val = self.evaluate(q.dequeue_many(4))
self.assertAllEqual(float_elems[4:8], float_val)
self.assertAllEqual(int_elems[4:8], int_val)

dequeued_single_t = q.dequeue()
float_val, int_val = self.evaluate(dequeued_single_t)
self.assertAllEqual(float_elems[8], float_val)
self.assertAllEqual(int_elems[8], int_val)
self.assertEqual(float_val.shape, dequeued_single_t[0].get_shape())
self.assertEqual(int_val.shape, dequeued_single_t[1].get_shape())
