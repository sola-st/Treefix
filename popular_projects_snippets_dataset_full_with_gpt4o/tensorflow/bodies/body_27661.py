# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
dataset = dataset_ops.Dataset.from_tensors(x)
dataset = dataset.repeat(math_ops.cast(x, dtype=dtypes.int64))
exit(dataset)
