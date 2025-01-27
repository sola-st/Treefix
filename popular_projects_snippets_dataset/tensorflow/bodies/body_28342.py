# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
dataset = dataset_ops.Dataset.range(elements).prefetch(
    buffer_size=buffer_size)
len_dataset = self.evaluate(dataset.cardinality())
expected_output = np.arange(elements)
for i in range(len_dataset):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)), expected_output[i])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=len_dataset))
