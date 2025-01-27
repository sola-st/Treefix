# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
components = (np.array([1, 2, 3], dtype=np.int64), (np.array([4., 5.]),
                                                    np.array([6., 7.])),
              np.array([8, 9, 10], dtype=np.int64))

dataset = dataset_ops.Dataset.from_tensors(components)
self.assertEqual(
    (dtypes.int64, (dtypes.float64, dtypes.float64), dtypes.int64),
    dataset_ops.get_legacy_output_types(dataset))
self.assertEqual(([3], ([2], [2]), [3]),
                 dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.shuffle(10, 10)
self.assertEqual(
    (dtypes.int64, (dtypes.float64, dtypes.float64), dtypes.int64),
    dataset_ops.get_legacy_output_types(dataset))
self.assertEqual(([3], ([2], [2]), [3]),
                 dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.repeat(-1)
self.assertEqual(
    (dtypes.int64, (dtypes.float64, dtypes.float64), dtypes.int64),
    dataset_ops.get_legacy_output_types(dataset))
self.assertEqual(([3], ([2], [2]), [3]),
                 dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.filter(lambda x, y, z: True)
self.assertEqual(
    (dtypes.int64, (dtypes.float64, dtypes.float64), dtypes.int64),
    dataset_ops.get_legacy_output_types(dataset))
self.assertEqual(([3], ([2], [2]), [3]),
                 dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.take(5)
self.assertEqual(
    (dtypes.int64, (dtypes.float64, dtypes.float64), dtypes.int64),
    dataset_ops.get_legacy_output_types(dataset))
self.assertEqual(([3], ([2], [2]), [3]),
                 dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.map(lambda x, y, z: ((x, z), (y[0], y[1])))
self.assertEqual(
    ((dtypes.int64, dtypes.int64), (dtypes.float64, dtypes.float64)),
    dataset_ops.get_legacy_output_types(dataset))
self.assertEqual((([3], [3]), ([2], [2])),
                 dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.flat_map(lambda x, y: dataset_ops.Dataset.from_tensors(
    ((x[0], x[1]), (y[0], y[1]))))
self.assertEqual(
    ((dtypes.int64, dtypes.int64), (dtypes.float64, dtypes.float64)),
    dataset_ops.get_legacy_output_types(dataset))
self.assertEqual((([3], [3]), ([2], [2])),
                 dataset_ops.get_legacy_output_shapes(dataset))

dataset = dataset.batch(32)
self.assertEqual(
    ((dtypes.int64, dtypes.int64), (dtypes.float64, dtypes.float64)),
    dataset_ops.get_legacy_output_types(dataset))
dataset_output_shapes = dataset_ops.get_legacy_output_shapes(dataset)
self.assertEqual(
    (([None, 3], [None, 3]), ([None, 2], [None, 2])),
    nest.pack_sequence_as(
        dataset_output_shapes,
        [s.as_list() for s in nest.flatten(dataset_output_shapes)]))

# Define a separate set of components with matching leading
# dimension for the from-slices constructor.
components_for_slices = (np.array([1, 2, 3],
                                  dtype=np.int64), (np.array([4., 5., 6.]),
                                                    np.array([7., 8., 9.])),
                         np.array([10, 11, 12], dtype=np.int64))

dataset = dataset_ops.Dataset.from_tensor_slices(components_for_slices)
self.assertEqual(
    (dtypes.int64, (dtypes.float64, dtypes.float64), dtypes.int64),
    dataset_ops.get_legacy_output_types(dataset))
self.assertEqual(([], ([], []), []),
                 dataset_ops.get_legacy_output_shapes(dataset))
