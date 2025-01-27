# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
elements = [{
    "foo": [1, 2, 3],
    "bar": [[4.0], [5.0], [6.0]]
}, {
    "foo": [4, 5, 6],
    "bar": [[7.0], [8.0], [9.0]]
}]
dataset = from_list.from_list(elements)
self.assertEqual(dtypes.int32,
                 dataset_ops.get_legacy_output_types(dataset)["foo"])
self.assertEqual(dtypes.float32,
                 dataset_ops.get_legacy_output_types(dataset)["bar"])
self.assertEqual((3,), dataset_ops.get_legacy_output_shapes(dataset)["foo"])
self.assertEqual((3, 1),
                 dataset_ops.get_legacy_output_shapes(dataset)["bar"])
self.assertDatasetProduces(dataset, expected_output=elements)
