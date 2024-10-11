# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
components = [
    np.tile(np.array([[1], [2], [3], [4]]), 20),
    np.tile(np.array([[12], [13], [14], [15]]), 22),
    np.array(arr)
]
datasets = [
    dataset_ops.Dataset.from_tensor_slices(component)
    for component in components
]
dataset = dataset_ops.Dataset.zip((datasets[0], (datasets[1], datasets[2])))
if options:
    dataset = dataset.with_options(options)
exit(dataset)
