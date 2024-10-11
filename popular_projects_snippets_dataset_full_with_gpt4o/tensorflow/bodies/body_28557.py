# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
input_components = (
    np.tile(np.array([[1], [2], [3], [4]]), 20),
    np.tile(np.array([[12], [13], [14], [15]]), 4))
to_concatenate_components = (
    np.tile(np.array([[1], [2], [3], [4], [5]]), 20),
    np.tile(np.array([[12], [13], [14], [15], [16]]), 15))

input_dataset = dataset_ops.Dataset.from_tensor_slices(input_components)
dataset_to_concatenate = dataset_ops.Dataset.from_tensor_slices(
    to_concatenate_components)
concatenated = input_dataset.concatenate(dataset_to_concatenate)
self.assertEqual(
    [ts.as_list()
     for ts in nest.flatten(
         dataset_ops.get_legacy_output_shapes(concatenated))],
    [[20], [None]])
get_next = self.getNext(concatenated)
for i in range(9):
    result = self.evaluate(get_next())
    if i < 4:
        for component, result_component in zip(input_components, result):
            self.assertAllEqual(component[i], result_component)
    else:
        for component, result_component in zip(to_concatenate_components,
                                               result):
            self.assertAllEqual(component[i - 4], result_component)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
