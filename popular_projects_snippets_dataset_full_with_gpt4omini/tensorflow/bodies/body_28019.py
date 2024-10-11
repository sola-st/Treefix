# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
dataset = dataset_ops.Dataset.range(elements).repeat(count_1).repeat(
    count_2)
expected_dataset = np.tile(
    np.arange(
        start=0, stop=elements, step=1, dtype=dtypes.int64.as_numpy_dtype),
    count_1 * count_2)
for i in range(elements * count_1 * count_2):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)),
        expected_dataset[i])
