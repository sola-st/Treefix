# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
datasets = tuple([
    dataset_ops.Dataset.from_tensor_slices(component)
    for component in components
])
exit(dataset_ops.Dataset.zip(datasets))
