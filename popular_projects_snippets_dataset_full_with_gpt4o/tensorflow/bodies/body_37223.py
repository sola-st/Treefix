# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
index = array_ops.placeholder(dtypes.int32)

# All inputs unknown.
p1 = array_ops.placeholder(dtypes.float32)
p2 = array_ops.placeholder(dtypes.float32)
p3 = array_ops.placeholder(dtypes.float32)
v1 = variables.VariableV1(p1, validate_shape=False)
v2 = variables.VariableV1(p2, validate_shape=False)
v3 = variables.VariableV1(p3, validate_shape=False)
self.assertIs(None, v1.get_shape().ndims)
s = control_flow_ops.ref_select(index, [v1, v2, v3])
self.assertIs(None, s.get_shape().ndims)

# All inputs known but different.
v1 = variables.VariableV1([[1, 2]])
v2 = variables.VariableV1([[2], [1]])
s = control_flow_ops.ref_select(index, [v1, v2])
self.assertIs(None, s.get_shape().ndims)

# All inputs known and same.
v1 = variables.VariableV1([[1, 2]])
v2 = variables.VariableV1([[1, 2]])
s = control_flow_ops.ref_select(index, [v1, v2])
self.assertEqual([1, 2], s.get_shape())

# Possibly the same but not guaranteed.
v1 = variables.VariableV1([[1., 2.]])
p2 = array_ops.placeholder(dtypes.float32, shape=[None, 2])
v2 = variables.VariableV1(p2, validate_shape=False)
s = control_flow_ops.ref_select(index, [v1, v2])
self.assertEqual(None, s.get_shape())
