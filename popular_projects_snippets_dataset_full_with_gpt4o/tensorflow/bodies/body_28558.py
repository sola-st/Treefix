# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_components = (
    np.tile(np.array([[1], [2], [3], [4]]), 5),
    np.tile(np.array([[12], [13], [14], [15]]), 4))
to_concatenate_components = (
    np.tile(np.array([[1], [2], [3], [4], [5]]), 20),
    np.tile(np.array([[12], [13], [14], [15], [16]]), 15),
    np.array([37.0, 38.0, 39.0, 40.0, 41.0]))

input_dataset = dataset_ops.Dataset.from_tensor_slices(input_components)
dataset_to_concatenate = dataset_ops.Dataset.from_tensor_slices(
    to_concatenate_components)

with self.assertRaisesRegex(TypeError, "Incompatible dataset elements"):
    input_dataset.concatenate(dataset_to_concatenate)
