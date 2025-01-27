# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py

components = [
    np.tile(np.array([[1], [2], [3], [4]]), 20),
    np.tile(np.array([[12], [13], [14], [15]]), 22),
    np.array([37.0, 38.0, 39.0, 40.0])
]
datasets = [
    dataset_ops.Dataset.from_tensor_slices(component)
    for component in components
]
dataset = dataset_ops.Dataset.zip((datasets[0], (datasets[1], datasets[2])))

self.assertEqual(
    dataset_ops.get_legacy_output_shapes(dataset),
    (tensor_shape.TensorShape([20]),
     (tensor_shape.TensorShape([22]), tensor_shape.TensorShape([]))))

get_next = self.getNext(dataset)
for i in range(4):
    result1, (result2, result3) = self.evaluate(get_next())
    self.assertAllEqual(components[0][i], result1)
    self.assertAllEqual(components[1][i], result2)
    self.assertAllEqual(components[2][i], result3)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
