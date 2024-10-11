# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
dataset = dataset_ops.Dataset.range(10).shuffle(
    10, seed=seed, reshuffle_each_iteration=reshuffle).repeat(2)
next_element = self.getNext(dataset)

first_epoch = []
for _ in range(10):
    first_epoch.append(self.evaluate(next_element()))

second_epoch = []
for _ in range(10):
    second_epoch.append(self.evaluate(next_element()))

self.assertEqual(first_epoch == second_epoch, not reshuffle)
