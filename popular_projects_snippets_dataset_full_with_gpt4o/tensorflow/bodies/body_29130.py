# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_spec_test.py
inner_spec = tensor_spec.TensorSpec(shape=(), dtype=dtypes.int32)
ds_spec = dataset_ops.DatasetSpec(inner_spec)
self.assertEqual(ds_spec.element_spec, inner_spec)
