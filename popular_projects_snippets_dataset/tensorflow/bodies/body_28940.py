# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
dataset = dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.range(1, 4), dataset_ops.Dataset.range(4, 7)))
expected_dataset = [(1, 4), (2, 5), (3, 6)]
for i in range(3):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)),
        expected_dataset[i])
