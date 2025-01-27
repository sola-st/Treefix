# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
components = np.random.randint(100, size=(200,)).astype(np.int64)
dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: x * x)
dataset = dataset.group_by_window(
    key_func=lambda x: x % 2,
    reduce_func=lambda _, xs: xs.batch(4),
    window_size=4)
get_next = self.getNext(dataset)
counts = []
with self.assertRaises(errors.OutOfRangeError):
    while True:
        result = self.evaluate(get_next())
        self.assertTrue(
            all(x % 2 == 0 for x in result) or all(x % 2 == 1) for x in result)
        counts.append(result.shape[0])

self.assertEqual(len(components), sum(counts))
num_full_batches = len([c for c in counts if c == 4])
self.assertGreaterEqual(num_full_batches, 24)
self.assertTrue(all(c == 4 for c in counts[:num_full_batches]))
