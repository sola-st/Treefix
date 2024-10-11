# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_spec_test.py
spec_1 = dataset_ops.DatasetSpec(
    tensor_spec.TensorSpec(shape=(1, None), dtype=dtypes.int32),
    [5, None, 2])
spec_2 = dataset_ops.DatasetSpec(
    tensor_spec.TensorSpec(shape=(None, None), dtype=dtypes.int32),
    [None, None, None])
spec_3 = dataset_ops.DatasetSpec(
    tensor_spec.TensorSpec(shape=(1, 2), dtype=dtypes.int32),
    [5, 3, 2])
spec_4 = dataset_ops.DatasetSpec(
    tensor_spec.TensorSpec(shape=(None, 2), dtype=dtypes.int32),
    [None, 1, None])

self.assertTrue(spec_1.is_subtype_of(spec_1))

self.assertTrue(spec_1.is_subtype_of(spec_2))
self.assertTrue(spec_3.is_subtype_of(spec_2))
self.assertTrue(spec_4.is_subtype_of(spec_2))

self.assertFalse(spec_2.is_subtype_of(spec_1))
self.assertFalse(spec_2.is_subtype_of(spec_3))
self.assertFalse(spec_2.is_subtype_of(spec_4))

self.assertEqual(spec_1.most_specific_common_supertype([]), spec_1)
self.assertEqual(spec_1.most_specific_common_supertype([spec_4]), spec_2)
self.assertEqual(
    spec_1.most_specific_common_supertype([spec_3, spec_4]), spec_2)
self.assertEqual(
    spec_1.most_specific_common_supertype([spec_2, spec_3, spec_4]), spec_2)
