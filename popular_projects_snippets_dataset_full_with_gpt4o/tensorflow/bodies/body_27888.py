# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
components = (variable_array, np.array([1, 2, 3]), np.array(37.0))
dataset = dataset_ops.Dataset.from_tensors(components)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
