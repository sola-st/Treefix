# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
exit(dataset_ops.Dataset.range(num_elements).apply(
    shuffle_ops.shuffle_and_repeat(buffer_size=5, count=count, seed=seed)))
