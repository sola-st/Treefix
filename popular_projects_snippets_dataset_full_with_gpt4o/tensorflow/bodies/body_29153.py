# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Tests randomly accessing elements of a dataset."""
# Tests accessing the elements in a shuffled order with repeats.
len_expected = len(expected)
indices = list(range(len_expected)) * 2
random.shuffle(indices)
for i in indices:
    self.assertAllEqual(expected[i],
                        self.evaluate(random_access.at(dataset, i)))

# Tests accessing the elements in order.
indices = set(sorted(indices))
for i in indices:
    self.assertAllEqual(expected[i],
                        self.evaluate(random_access.at(dataset, i)))
