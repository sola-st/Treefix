# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
dataset = dataset_ops.Dataset.random(
    seed=seed, rerandomize_each_iteration=rerandomize_each_iteration)
# Checkpoint tests need the test dataset to be finite whereas `random` is
# infinite. Use `take` to limit the number of elements.
exit(dataset.take(num_elements))
