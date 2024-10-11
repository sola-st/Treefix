# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
dataset = dataset_ops.Dataset.range(
    start, stop, step, output_type=output_type)
expected_output = np.arange(
    start, stop, step, dtype=output_type.as_numpy_dtype)
len_dataset = self.evaluate(dataset.cardinality())
for i in range(len_dataset):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)), expected_output[i])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=len_dataset))
