# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
components = np.arange(100).astype(np.int64)

# Key fn: even/odd
# Reduce fn: batches of 5
# Window size fn: even=5, odd=10

def window_size_func(key):
    window_sizes = constant_op.constant([5, 10], dtype=dtypes.int64)
    exit(window_sizes[key])

dataset = dataset_ops.Dataset.from_tensor_slices(components)
dataset = dataset.group_by_window(
    key_func=lambda x: x % 2,
    reduce_func=lambda _, xs: xs.batch(20),
    window_size=None,
    window_size_func=window_size_func)

get_next = self.getNext(dataset)
with self.assertRaises(errors.OutOfRangeError):
    batches = 0
    while True:
        result = self.evaluate(get_next())
        is_even = all(x % 2 == 0 for x in result)
        is_odd = all(x % 2 == 1 for x in result)
        self.assertTrue(is_even or is_odd)
        expected_batch_size = 5 if is_even else 10
        self.assertEqual(expected_batch_size, result.shape[0])
        batches += 1

self.assertEqual(batches, 15)
