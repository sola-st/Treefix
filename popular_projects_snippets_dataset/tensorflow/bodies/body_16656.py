# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
spec = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False)
spec2 = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False)
self.assertEqual(spec, spec2)
# Test alias_id=None
spec3 = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False, 1)
self.assertNotEqual(spec, spec3)
spec4 = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False, 1)
self.assertEqual(spec3, spec4)
# Test shape
spec5 = resource_variable_ops.VariableSpec([1, 5], dtypes.float32, False, 1)
self.assertNotEqual(spec4, spec5)
# Test dtype
spec6 = resource_variable_ops.VariableSpec([1, 3], dtypes.int32, False, 1)
self.assertNotEqual(spec4, spec6)
# Test trainable
spec7 = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, True, 1)
self.assertNotEqual(spec7, spec4)
# Test alias_id
spec8 = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False, 2)
self.assertNotEqual(spec8, spec4)
