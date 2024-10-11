# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, (dtypes_lib.float32, dtypes_lib.int32))
float_elems = [10.0, 20.0, 30.0, 40.0]
int_elems = [[1, 2], [3, 4], [5, 6], [7, 8]]

self.evaluate(q.enqueue_many((float_elems, int_elems)))
self.evaluate(q.enqueue_many((float_elems, int_elems)))

for i in range(8):
    float_val, int_val = self.evaluate(q.dequeue())
    self.assertEqual(float_elems[i % 4], float_val)
    self.assertAllEqual(int_elems[i % 4], int_val)
