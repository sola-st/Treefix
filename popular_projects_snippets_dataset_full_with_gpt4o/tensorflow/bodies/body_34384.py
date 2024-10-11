# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, (dtypes_lib.int32, dtypes_lib.float32))
elems = [(5, 10.0), (10, 20.0), (15, 30.0)]

for x in elems:
    self.evaluate(q.enqueue(x))

for i in range(len(elems)):
    x_val, y_val = self.evaluate(q.dequeue())
    x, y = elems[i]
    self.assertEqual([x], x_val)
    self.assertEqual([y], y_val)
