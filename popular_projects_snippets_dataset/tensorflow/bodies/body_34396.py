# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(
    10, (dtypes_lib.float32, dtypes_lib.int32), shapes=((), (2,)))
float_elems = [
    10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0
]
int_elems = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14],
             [15, 16], [17, 18], [19, 20]]

self.evaluate(q.enqueue_many((float_elems, int_elems)))

dequeued_t = q.dequeue_up_to(4)
float_val, int_val = self.evaluate(dequeued_t)
self.assertAllEqual(float_elems[0:4], float_val)
self.assertAllEqual(int_elems[0:4], int_val)
if not context.executing_eagerly():
    self.assertEqual([None], dequeued_t[0].get_shape().as_list())
    self.assertEqual([None, 2], dequeued_t[1].get_shape().as_list())

float_val, int_val = self.evaluate(q.dequeue_up_to(4))
self.assertAllEqual(float_elems[4:8], float_val)
self.assertAllEqual(int_elems[4:8], int_val)
