# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
spec = resource_variable_ops.VariableSpec([1, 3], dtypes.float32)
self.assertIs(spec.value_type, resource_variable_ops.ResourceVariable)
