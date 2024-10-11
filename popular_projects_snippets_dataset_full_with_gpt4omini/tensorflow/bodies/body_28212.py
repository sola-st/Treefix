# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
elements = np.random.randint(100, size=[200])
queue = data_flow_ops.FIFOQueue(200, dtypes.int64, shapes=[])
enqueue_op = queue.enqueue_many(elements)
close_op = queue.close()
dataset = dataset_ops.Dataset.from_tensors(0).repeat(-1)
dataset = apply_map(dataset, lambda _: queue.dequeue())

get_next = self.getNext(dataset, requires_initialization=True)
self.evaluate(enqueue_op)
self.evaluate(close_op)

for element in elements:
    self.assertEqual(element, self.evaluate(get_next()))
# When the map function in `MapDataset` raises an OutOfRange error, TF1 and
# TF2 behave differently. TF1 raises an OutOfRangeError to signal the end of
# sequence while TF2 raises an InvalidArgumentError. This behavior is
# controlled by the `preserve_cardinality` argument of `map` transformation
# which is set to `True` for TF2 and `False` for TF1, which is for backward
# compatibility.
if tf2.enabled():
    with self.assertRaises(errors.InvalidArgumentError):
        self.evaluate(get_next())
else:
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())
