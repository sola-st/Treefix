# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
components = (np.array(1), np.array([1, 2, 3]), np.array(37.0),
              sparse_tensor.SparseTensorValue(
                  indices=np.array([[0]]),
                  values=np.array([0]),
                  dense_shape=np.array([1])),
              sparse_tensor.SparseTensorValue(
                  indices=np.array([[0, 0], [1, 1]]),
                  values=np.array([-1, 1]),
                  dense_shape=np.array([2, 2])),
              ragged_factory_ops.constant_value([[[0]], [[1]], [[2]]]))

dataset = dataset_ops.Dataset.from_tensors(components)

self.assertDatasetProduces(dataset, expected_output=[components])
