# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_components = {
    "foo": np.array([[1], [2], [3], [4]]),
    "bar": np.array([[12], [13], [14], [15]])
}
to_concatenate_components = {
    "foo": np.array([[1], [2], [3], [4]]),
    "baz": np.array([[5], [6], [7], [8]])
}

input_dataset = dataset_ops.Dataset.from_tensor_slices(input_components)
dataset_to_concatenate = dataset_ops.Dataset.from_tensor_slices(
    to_concatenate_components)

with self.assertRaisesRegex(TypeError, "Incompatible dataset elements"):
    input_dataset.concatenate(dataset_to_concatenate)
