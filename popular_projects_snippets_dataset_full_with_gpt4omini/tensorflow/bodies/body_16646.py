# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
spec = VariableSpec(shape=None)
spec2 = VariableSpec(shape=[None, 15])
spec3 = VariableSpec(shape=[None])

self.assertTrue(spec.is_compatible_with(spec2))
self.assertFalse(spec2.is_compatible_with(spec3))

var = resource_variable_ops.ResourceVariable(
    initial_value=np.ones((3, 15), dtype=np.float32))
var2 = resource_variable_ops.ResourceVariable(
    initial_value=np.ones((3,), dtype=np.int32))

self.assertTrue(spec.is_compatible_with(var))
self.assertFalse(spec2.is_compatible_with(var2))

spec4 = VariableSpec(shape=None, dtype=dtypes.int32)
spec5 = VariableSpec(shape=[None], dtype=dtypes.int32)

self.assertFalse(spec.is_compatible_with(spec4))
self.assertTrue(spec4.is_compatible_with(spec5))
self.assertTrue(spec4.is_compatible_with(var2))

tensor = constant_op.constant([1, 2, 3])
self.assertFalse(spec4.is_compatible_with(tensor))
