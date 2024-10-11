# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
dataset = dataset_ops.Dataset.range(elements).repeat(count)
expected_dataset = np.tile(
    np.arange(
        start=0, stop=elements, step=1, dtype=dtypes.int64.as_numpy_dtype),
    count)
for i in range(elements * count):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)),
        expected_dataset[i])
