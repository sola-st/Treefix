# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
dataset = dataset_ops.Dataset.random(
    seed=42, rerandomize_each_iteration=rerandomize, name="random").take(10)
first_epoch = self.getDatasetOutput(dataset)
second_epoch = self.getDatasetOutput(dataset)

if rerandomize:
    self.assertEqual(first_epoch == second_epoch,
                     not rerandomize or rerandomize is None)
else:
    self.assertEqual(first_epoch, second_epoch)
