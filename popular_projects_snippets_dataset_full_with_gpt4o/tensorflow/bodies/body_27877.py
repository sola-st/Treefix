# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
"""Test a dataset that represents a single tuple of tensors."""
components = (sparse_tensor.SparseTensorValue(
    indices=np.array([[0]]),
    values=np.array([0]),
    dense_shape=np.array([1])),
              sparse_tensor.SparseTensorValue(
                  indices=np.array([[0, 0], [1, 1]]),
                  values=np.array([-1, 1]),
                  dense_shape=np.array([2, 2])))

dataset = dataset_ops.Dataset.from_tensors(components)

self.assertEqual(
    [tensor_shape.TensorShape(c.dense_shape) for c in components],
    [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])
self.assertDatasetProduces(dataset, expected_output=[components])
