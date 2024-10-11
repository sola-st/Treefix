# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
elements = np.random.randint(100, size=[200])
queue = data_flow_ops.FIFOQueue(
    200, dtypes.int64, shapes=[], shared_name="shared_queue")
queue_2 = data_flow_ops.FIFOQueue(
    200, dtypes.int64, shapes=[], shared_name="shared_queue")

enqueue_op = queue.enqueue_many(elements)
close_op = queue.close()

dataset = dataset_ops.Dataset.from_tensors(0).repeat(-1)
dataset = apply_map(dataset, lambda _: (queue.dequeue(), queue_2.dequeue()))

self.evaluate(enqueue_op)
self.evaluate(close_op)
get_next = self.getNext(dataset, requires_initialization=True)
for i in range(100):
    self.assertCountEqual([elements[i * 2], elements[i * 2 + 1]],
                          self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
