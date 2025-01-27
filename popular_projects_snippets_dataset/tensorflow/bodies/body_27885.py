# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
components = np.array([1, 2, 3], dtype=np.int64)

dataset = dataset_ops.Dataset.from_tensors(components)
self.assertEqual(dtypes.int64,
                 dataset_ops.get_legacy_output_types(dataset))
self.assertEqual([3], dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.filter(
    lambda x: math_ops.reduce_all(math_ops.equal(x, components)))
self.assertEqual(dtypes.int64,
                 dataset_ops.get_legacy_output_types(dataset))
self.assertEqual([3], dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.map(lambda x: array_ops.stack([x, x]))
self.assertEqual(dtypes.int64,
                 dataset_ops.get_legacy_output_types(dataset))
self.assertEqual([2, 3], dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.flat_map(
    lambda x: dataset_ops.Dataset.from_tensor_slices(x))
self.assertEqual(dtypes.int64,
                 dataset_ops.get_legacy_output_types(dataset))
self.assertEqual([3], dataset_ops.get_legacy_output_shapes(dataset))

get_next = self.getNext(dataset)
self.assertEqual(dtypes.int64, get_next().dtype)
self.assertEqual([3], get_next().shape)
