# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
dataset_1 = dataset_ops.DatasetV2.from_tensor_slices([False, True, False])
dataset_2 = dataset_ops.DatasetV2.from_tensor_slices([True, True, True])
self.assertEqual(self.evaluate(py_builtins.all_(dataset_1)), False)
self.assertEqual(self.evaluate(py_builtins.all_(dataset_2)), True)

dataset_3 = dataset_ops.DatasetV2.from_tensor_slices([0, 1, 2])
with self.assertRaises(ValueError):
    py_builtins.all_(dataset_3)

dataset_4 = dataset_ops.DatasetV2.from_tensor_slices([False, True, False])
dataset_zipped = dataset_ops.DatasetV2.zip((dataset_4, dataset_4))
with self.assertRaises(ValueError):
    py_builtins.all_(dataset_zipped)

dataset_mixed = dataset_ops.DatasetV2.zip((dataset_3, dataset_4))
with self.assertRaises(ValueError):
    py_builtins.all_(dataset_mixed)
