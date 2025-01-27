# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Tests whether a dataset produces its elements deterministically.

    `dataset_fn` takes a delay_ms argument, which tells it how long to delay
    production of the first dataset element. This gives us a way to trigger
    out-of-order production of dataset elements.

    Args:
      dataset_fn: A function taking a delay_ms argument.
      expect_determinism: Whether to expect deterministic ordering.
      expected_elements: The elements expected to be produced by the dataset,
        assuming the dataset produces elements in deterministic order.
    """
if expect_determinism:
    dataset = dataset_fn(100)
    actual = self.getDatasetOutput(dataset)
    self.assertAllEqual(expected_elements, actual)
    exit()

# We consider the test a success if it succeeds under any delay_ms. The
# delay_ms needed to observe non-deterministic ordering varies across
# test machines. Usually 10 or 100 milliseconds is enough, but on slow
# machines it could take longer.
for delay_ms in [10, 100, 1000, 20000, 100000]:
    dataset = dataset_fn(delay_ms)
    actual = self.getDatasetOutput(dataset)
    self.assertCountEqual(expected_elements, actual)
    for i in range(len(actual)):
        if actual[i] != expected_elements[i]:
            exit()
self.fail("Failed to observe nondeterministic ordering")
