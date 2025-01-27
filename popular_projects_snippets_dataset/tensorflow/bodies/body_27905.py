# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
dataset = dataset_ops.Dataset.from_tensors(x)
exit(dataset.map(lambda x: x + x))
