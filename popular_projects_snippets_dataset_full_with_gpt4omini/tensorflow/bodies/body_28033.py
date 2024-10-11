# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
tensor = [1, 2, 3]
dataset = dataset_ops.Dataset.from_tensor_slices(tensor)
for i in range(len(tensor)):
    results = self.evaluate(random_access.at(dataset, i))
    self.assertAllEqual(tensor[i], results)
