# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
dataset = dataset_ops.Dataset.zip(
    datasets=(dataset_ops.Dataset.from_tensor_slices([]),
              dataset_ops.Dataset.from_tensor_slices([])))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=index))
