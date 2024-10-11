# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_spec_test.py
spec_1 = dataset_ops.DatasetSpec(
    {"a": tensor_spec.TensorSpec(shape=(1, None), dtype=dtypes.int32)},
    [])
spec_2 = dataset_ops.DatasetSpec(
    {"a": tensor_spec.TensorSpec(shape=(None, None), dtype=dtypes.int32)},
    [])
spec_3 = dataset_ops.DatasetSpec(
    {"b": tensor_spec.TensorSpec(shape=(1, None), dtype=dtypes.int32)},
    [])
spec_4 = dataset_ops.DatasetSpec({"b": None}, [])

self.assertTrue(spec_1.is_subtype_of(spec_1))
self.assertTrue(spec_1.is_subtype_of(spec_2))
self.assertFalse(spec_2.is_subtype_of(spec_1))

self.assertFalse(spec_1.is_subtype_of(spec_3))
self.assertFalse(spec_3.is_subtype_of(spec_1))
self.assertFalse(spec_2.is_subtype_of(spec_3))
self.assertFalse(spec_3.is_subtype_of(spec_2))

self.assertTrue(spec_4.is_subtype_of(spec_4))
self.assertEqual(spec_4.most_specific_common_supertype([]), spec_4)
self.assertEqual(spec_4.most_specific_common_supertype([spec_4]), spec_4)
