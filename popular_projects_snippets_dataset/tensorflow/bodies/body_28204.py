# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
components = np.array([1., 2., 3., np.nan, 5.]).astype(np.float32)

dataset = dataset_ops.Dataset.from_tensor_slices(components)
dataset = apply_map(
    dataset,
    lambda x: array_ops.check_numerics(x, "message"),
    num_parallel_calls=2)
get_next = self.getNext(dataset)

for _ in range(3):
    self.evaluate(get_next())
