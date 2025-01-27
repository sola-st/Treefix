# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
dataset = dataset_ops.Dataset.random(
    seed=42, rerandomize_each_iteration=rerandomize, name="random").take(10)
dataset = dataset.repeat(2)
next_element = self.getNext(dataset, requires_initialization=True)
first_epoch = []
for _ in range(10):
    first_epoch.append(self.evaluate(next_element()))
second_epoch = []
for _ in range(10):
    second_epoch.append(self.evaluate(next_element()))

if rerandomize:
    self.assertEqual(first_epoch == second_epoch,
                     not rerandomize or rerandomize is None)
else:
    self.assertEqual(first_epoch, second_epoch)
