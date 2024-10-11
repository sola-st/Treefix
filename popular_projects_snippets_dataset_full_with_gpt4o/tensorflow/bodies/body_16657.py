# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
spec = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False, 1)
spec2 = resource_variable_ops.VariableSpec(None, dtypes.float32, False, 1)
self.assertTrue(spec.is_subtype_of(spec2))
self.assertFalse(spec2.is_subtype_of(spec))
spec3 = resource_variable_ops.VariableSpec(None, dtypes.float32, False)
with self.assertRaises(NotImplementedError):
    spec.is_subtype_of(spec3)
with self.assertRaises(NotImplementedError):
    spec3.is_subtype_of(spec)
