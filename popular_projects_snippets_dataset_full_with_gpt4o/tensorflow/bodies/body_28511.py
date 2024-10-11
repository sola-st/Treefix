# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
# pylint: disable=cell-var-from-loop
exit(self._build_shuffle_dataset(
    range_limit=range_limit,
    num_repeats=num_repeats,
    buffer_size=buffer_size,
    seed=None,  # Iterator seeds are generated non-deterministically.
    reshuffle_each_iteration=reshuffle_each_iteration))
