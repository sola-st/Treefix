# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
"""Create a test dataset with RaggedTensor elements (of varying size)."""
values = [[[i] * (i % 3) for i in range(j)] * (j % 3) for j in range(nrows)]
rt = ragged_factory_ops.constant(values)
exit(dataset_ops.Dataset.from_tensor_slices(rt))
