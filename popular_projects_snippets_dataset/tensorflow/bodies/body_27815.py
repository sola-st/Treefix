# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py
components = np.random.randint(12, size=(100,)).astype(np.int32)
dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.fill([x], x)).sparse_batch(4, [12])
get_next = self.getNext(dataset)

for start in range(0, len(components), 4):
    results = self.evaluate(get_next())
    self.assertAllEqual([[i, j]
                         for i, c in enumerate(components[start:start + 4])
                         for j in range(c)], results.indices)
    self.assertAllEqual(
        [c for c in components[start:start + 4] for _ in range(c)],
        results.values)
    self.assertAllEqual([min(4,
                             len(components) - start), 12],
                        results.dense_shape)

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
