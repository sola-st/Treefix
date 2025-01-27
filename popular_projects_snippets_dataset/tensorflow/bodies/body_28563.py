# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_components = (np.tile(np.array([[1], [2], [3], [4]]), 20),
                    np.tile(np.array([[12], [13], [14], [15]]), 4))
to_concatenate_components = (np.tile(
    np.array([[5], [6], [7], [8], [9]]), 20), var_array)

dataset = dataset_ops.Dataset.from_tensor_slices(
    input_components).concatenate(
        dataset_ops.Dataset.from_tensor_slices(to_concatenate_components))
if options:
    dataset = dataset.with_options(options)
exit(dataset)
