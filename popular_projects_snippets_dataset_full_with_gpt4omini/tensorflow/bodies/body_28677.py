# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
# Tests that an exception is raised (as opposed to a segfault) when the
# Python structure assigned to a dataset is incorrect.
dataset = dataset_ops.Dataset.range(10)
spec = tensor_spec.TensorSpec([], dtypes.int64)
new_structure = (spec, spec)
dataset = dataset_ops._RestructuredDataset(dataset, new_structure)
dataset = dataset.map(lambda x, y: y)

with self.assertRaisesOpError(""):
    self.getDatasetOutput(dataset)
