# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
seed = 55
num_elements = 10
# pylint: disable=g-long-lambda
verify_fn(
    self,
    lambda: self._build_random_dataset(
        seed=seed,
        num_elements=num_elements,
        rerandomize_each_iteration=rerandomize_each_iteration),
    num_elements)
