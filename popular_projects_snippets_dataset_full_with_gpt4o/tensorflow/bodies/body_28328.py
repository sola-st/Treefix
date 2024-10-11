# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([0, 1, 2, 3, 4,
                                                  5]).map(lambda x: x * 3)
for i in range(5):
    self.assertEqual(self.evaluate(random_access.at(dataset, index=i)), i * 3)
