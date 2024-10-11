# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
"""Validates results from a `make_coordinted_read_dataset` dataset.

    Each group of `num_consumers` results should be consecutive, indicating that
    they were produced by the same worker.

    Args:
      results: The elements produced by the dataset.
      num_consumers: The number of consumers.
    """
groups = [
    results[start:start + num_consumers]
    for start in range(0, len(results), num_consumers)
]
incorrect_groups = []
for group in groups:
    # Check that each group of `num_consumers` results are consecutive.
    for offset in range(1, len(group)):
        if group[0] + offset != group[offset]:
            incorrect_groups.append(group)
            break
self.assertEmpty(
    incorrect_groups,
    "Incorrect groups: {}.\nAll groups: {}".format(incorrect_groups,
                                                   groups))
