# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_components = (
    np.tile(np.array([[1], [2], [3], [4]]), 5),
    np.tile(np.array([[12], [13], [14], [15]]), 4))
to_concatenate_components = (
    np.tile(np.array([[1.0], [2.0], [3.0], [4.0]]), 5),
    np.tile(np.array([[12], [13], [14], [15]]), 15))

input_dataset = dataset_ops.Dataset.from_tensor_slices(input_components)
dataset_to_concatenate = dataset_ops.Dataset.from_tensor_slices(
    to_concatenate_components)

with self.assertRaisesRegex(TypeError, "Incompatible dataset elements"):
    input_dataset.concatenate(dataset_to_concatenate)
