# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
repeat_dataset = (
    dataset_ops.Dataset.from_tensor_slices(components).repeat(count))
if filename:
    exit(repeat_dataset.cache(filename))
else:
    exit(repeat_dataset)
