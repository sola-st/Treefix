# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
components = {"foo": [1, 2, 3], "bar": [[4.0], [5.0], [6.0]]}
dataset = dataset_ops.Dataset.from_tensor_slices(components)
get_next = self.getNext(dataset)

self.assertEqual(dtypes.int32,
                 dataset_ops.get_legacy_output_types(dataset)["foo"])
self.assertEqual(dtypes.float32,
                 dataset_ops.get_legacy_output_types(dataset)["bar"])
self.assertEqual((), dataset_ops.get_legacy_output_shapes(dataset)["foo"])
self.assertEqual((1,), dataset_ops.get_legacy_output_shapes(dataset)["bar"])

for i in range(3):
    results = self.evaluate(get_next())
    self.assertEqual(components["foo"][i], results["foo"])
    self.assertEqual(components["bar"][i], results["bar"])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
