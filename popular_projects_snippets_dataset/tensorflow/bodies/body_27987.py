# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
dataset = dataset_ops.Dataset.random(
    seed=42,
    rerandomize_each_iteration=rerandomize,
    name="random").take(10)
exit(dataset)
