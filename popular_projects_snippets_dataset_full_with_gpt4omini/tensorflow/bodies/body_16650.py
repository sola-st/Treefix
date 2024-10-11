# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
spec = resource_variable_ops.VariableSpec(shape=[1], dtype=dtypes.float32)
self.assertRaisesRegex(TypeError, "must be a list or tuple",
                       spec._from_components, constant_op.constant(1.))
self.assertRaisesRegex(ValueError,
                       "must only contain its resource handle",
                       spec._from_components,
                       [constant_op.constant(1.), constant_op.constant(2.)])
self.assertRaisesRegex(ValueError, "must be a resource tensor",
                       spec._from_components, [constant_op.constant(1.)])
