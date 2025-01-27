# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
v = variable_scope.get_variable(
    name="v", initializer=[1.], use_resource=True)
mirrored = values_lib.MirroredVariable(
    None, (v,), variable_scope.VariableAggregation.MEAN)

self.assertEqual(v.name, mirrored.name)
self.assertEqual(v.dtype, mirrored.dtype)
self.assertEqual(v.shape, mirrored.shape)
