# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
components = {"a": {"aa": 1, "ab": [2.0, 2.0]}, "b": [3, 3, 3]}
dataset = dataset_ops.Dataset.from_tensors(components)
self.assertEqual(dtypes.int32,
                 dataset_ops.get_legacy_output_types(dataset)["a"]["aa"])
self.assertEqual(dtypes.float32,
                 dataset_ops.get_legacy_output_types(dataset)["a"]["ab"])
self.assertEqual(dtypes.int32,
                 dataset_ops.get_legacy_output_types(dataset)["b"])
self.assertEqual([],
                 dataset_ops.get_legacy_output_shapes(dataset)["a"]["aa"])
self.assertEqual([2],
                 dataset_ops.get_legacy_output_shapes(dataset)["a"]["ab"])
self.assertEqual([3],
                 dataset_ops.get_legacy_output_shapes(dataset)["b"])
