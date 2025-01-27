# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
var = resource_variable_ops.ResourceVariable(1.0)
types, tensors = execute_lib.convert_to_mixed_eager_tensors(
    ['foo', var], context.context())
self.assertAllEqual([dtypes.string, dtypes.float32], types)
for t in tensors:
    self.assertIsInstance(t, ops.EagerTensor)
