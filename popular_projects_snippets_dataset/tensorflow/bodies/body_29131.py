# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_spec_test.py
trace_type_1 = dataset_ops.DatasetSpec(
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.int32),
    [5])
trace_type_2 = dataset_ops.DatasetSpec(
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.int32),
    [5])

self.assertEqual(trace_type_1, trace_type_2)
self.assertEqual(hash(trace_type_1), hash(trace_type_2))
self.assertTrue(trace_type_1.is_subtype_of(trace_type_2))
self.assertTrue(trace_type_2.is_subtype_of(trace_type_1))

trace_type_3 = dataset_ops.DatasetSpec(
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.int32),
    [6])
self.assertNotEqual(trace_type_1, trace_type_3)
self.assertFalse(trace_type_1.is_subtype_of(trace_type_3))
self.assertFalse(trace_type_3.is_subtype_of(trace_type_1))
