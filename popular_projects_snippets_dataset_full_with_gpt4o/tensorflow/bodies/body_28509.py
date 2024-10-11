# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
exit(dataset_ops.Dataset.range(range_limit).shuffle(
    buffer_size,
    seed=seed,
    reshuffle_each_iteration=reshuffle_each_iteration).repeat(num_repeats))
