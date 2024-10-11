# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
ds1 = dataset_ops.Dataset.range(0)
ds2 = ds1.concatenate(ds1)
ds3 = dataset_ops.Dataset.zip((ds2, ds1, ds2))

inputs = []
queue = [ds3]
while queue:
    ds = queue[0]
    queue = queue[1:]
    queue.extend(ds._inputs())
    inputs.append(ds)

self.assertEqual(5, inputs.count(ds1))
self.assertEqual(2, inputs.count(ds2))
self.assertEqual(1, inputs.count(ds3))
