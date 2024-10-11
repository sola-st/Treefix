# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
dataset = dataset_ops.Dataset.range(10)

first_epoch = []
for elem in dataset.shuffle(
    10, seed=seed, reshuffle_each_iteration=reshuffle):
    first_epoch.append(elem.numpy())

second_epoch = []
for elem in dataset.shuffle(
    10, seed=seed, reshuffle_each_iteration=reshuffle):
    second_epoch.append(elem.numpy())

self.assertEqual(first_epoch != second_epoch, seed is None)
