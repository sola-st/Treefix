# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
q = data_flow_ops.FIFOQueue(10, dtypes_lib.float16)
elems = [10.0, 20.0, 30.0]

for x in elems:
    self.evaluate(q.enqueue((x,)))

for i in range(len(elems)):
    vals = self.evaluate(q.dequeue())
    self.assertEqual([elems[i]], vals)
