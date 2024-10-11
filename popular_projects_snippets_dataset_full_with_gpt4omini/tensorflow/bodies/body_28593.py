# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py

# Check that a dataset which produces random permutation of range(10) ends
# up being cached when we read all of its element but do not reach EOF.
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.shuffle(10, reshuffle_each_iteration=True).cache()

it = iter(dataset)

results = []
for _ in range(10):
    results.append(next(it))

it = iter(dataset)
for i in range(10):
    self.assertEqual(next(it), results[i])
