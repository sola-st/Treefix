# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
"""Test a dataset that represents the slices from a tuple of tensors."""
components = (np.tile(np.array([[1], [2], [3]]), 20),
              np.tile(np.array([[12], [13], [14]]), 22),
              np.array([37.0, 38.0, 39.0]),
              sparse_tensor.SparseTensorValue(
                  indices=np.array([[0, 0], [1, 0], [2, 0]]),
                  values=np.array([0, 0, 0]),
                  dense_shape=np.array([3, 1])),
              sparse_tensor.SparseTensorValue(
                  indices=np.array([[0, 0], [1, 1], [2, 2]]),
                  values=np.array([1, 2, 3]),
                  dense_shape=np.array([3, 3])))

dataset = dataset_ops.Dataset.from_tensor_slices(components)
get_next = self.getNext(dataset)
self.assertEqual([
    tensor_shape.TensorShape(c.dense_shape[1:])
    if sparse_tensor.is_sparse(c) else c.shape[1:] for c in components
], [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])

expected = [
    (sparse_tensor.SparseTensorValue(
        indices=np.array([[0]]),
        values=np.array([0]),
        dense_shape=np.array([1])),
     sparse_tensor.SparseTensorValue(
         indices=np.array([[0]]),
         values=np.array([1]),
         dense_shape=np.array([3]))),
    (sparse_tensor.SparseTensorValue(
        indices=np.array([[0]]),
        values=np.array([0]),
        dense_shape=np.array([1])),
     sparse_tensor.SparseTensorValue(
         indices=np.array([[1]]),
         values=np.array([2]),
         dense_shape=np.array([3]))),
    (sparse_tensor.SparseTensorValue(
        indices=np.array([[0]]),
        values=np.array([0]),
        dense_shape=np.array([1])),
     sparse_tensor.SparseTensorValue(
         indices=np.array([[2]]),
         values=np.array([3]),
         dense_shape=np.array([3]))),
]
for i in range(3):
    results = self.evaluate(get_next())
    for component, result_component in zip(
        (list(zip(*components[:3]))[i] + expected[i]), results):
        self.assertValuesEqual(component, result_component)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
