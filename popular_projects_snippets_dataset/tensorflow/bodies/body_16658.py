# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
spec = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False, 1)
spec2 = resource_variable_ops.VariableSpec([1, 2], dtypes.float32, False, 1)
spec3 = spec.most_specific_common_supertype([spec2])
expected_spec = resource_variable_ops.VariableSpec(
    [1, None], dtypes.float32, False, 1)
self.assertEqual(spec3, expected_spec)

spec4 = resource_variable_ops.VariableSpec([1, 3], dtypes.float32, False)
spec5 = resource_variable_ops.VariableSpec([1, 2], dtypes.float32, False)
spec6 = spec4.most_specific_common_supertype([spec5])
expected_spec = resource_variable_ops.VariableSpec(
    [1, None], dtypes.float32, False)
self.assertEqual(spec6, expected_spec)

with self.assertRaises(NotImplementedError):
    spec.most_specific_common_supertype([spec4])
with self.assertRaises(NotImplementedError):
    spec4.most_specific_common_supertype([spec])
