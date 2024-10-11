# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
seed = 55
range_limit = 5
num_repeats = 2
num_outputs = range_limit * num_repeats
# pylint: disable=g-long-lambda
verify_fn(
    self, lambda: self._build_shuffle_dataset(
        range_limit=range_limit,
        num_repeats=num_repeats,
        buffer_size=buffer_size,
        seed=seed,
        reshuffle_each_iteration=reshuffle_each_iteration), num_outputs)
