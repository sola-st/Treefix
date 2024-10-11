# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
data = tuple([(math_ops.range(10),) for _ in range(3)])
data = dataset_ops.Dataset.from_tensor_slices(data)
expected_types = ((dtypes.int32,),) * 3
data = data.batch(2)
self.assertEqual(expected_types, dataset_ops.get_legacy_output_types(data))
data = data.unbatch()
self.assertEqual(expected_types, dataset_ops.get_legacy_output_types(data))

self.assertDatasetProduces(data, [((i,),) * 3 for i in range(10)])
