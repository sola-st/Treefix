# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(2.0)
w = resource_variable_ops.ResourceVariable.from_proto(v.to_proto())
self.assertIsInstance(w.dtype, dtypes.DType)
self.assertEqual(v.dtype, w.dtype)
