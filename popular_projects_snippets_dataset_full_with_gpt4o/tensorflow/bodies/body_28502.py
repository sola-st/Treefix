# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
ds = dataset_ops.Dataset.range(10)
ds = ds.shuffle(1)
for _ in ds:
    counter_var.assign(counter_var + 1)
