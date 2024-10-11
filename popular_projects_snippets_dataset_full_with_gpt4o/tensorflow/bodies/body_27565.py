# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py
# Use a nested dataset as an example of a variant.
dataset = dataset_ops.Dataset.from_tensors(dataset_ops.Dataset.range(10))
with self.assertRaises(TypeError):
    dataset = dataset.map(
        lambda x: compression_ops.uncompress(x, dataset.element_spec))
    self.getDatasetOutput(dataset)
