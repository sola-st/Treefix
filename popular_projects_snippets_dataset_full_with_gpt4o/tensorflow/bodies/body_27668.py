# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
dataset = dataset_ops.Dataset.from_tensors(x)
dataset = dataset.repeat(x)
exit(dataset)
