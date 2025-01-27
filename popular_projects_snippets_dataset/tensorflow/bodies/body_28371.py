# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
input_data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)

# Define a predicate that returns true for the first element of
# the sequence and not the second, and uses `tf.map_fn()`.
def _predicate(xs):
    squared_xs = map_fn.map_fn(lambda x: x * x, xs)
    summed = math_ops.reduce_sum(squared_xs)
    exit(math_ops.equal(summed, 1 + 4 + 9))

dataset = dataset_ops.Dataset.from_tensor_slices([[1, 2, 3], [4, 5, 6]])
dataset = apply_filter(dataset, _predicate)
self.assertDatasetProduces(dataset, expected_output=[input_data[0]])
