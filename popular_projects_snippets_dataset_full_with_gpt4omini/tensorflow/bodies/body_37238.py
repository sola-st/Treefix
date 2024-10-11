# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
st1 = sparse_tensor.SparseTensor([[0, 5]], ['x'], [10, 10])
st2 = control_flow_ops._Enter(st1, "foo_1")
st3 = control_flow_ops.exit(st2)
self.assertAllEqual(st1.indices, st3.indices)
self.assertAllEqual(st1.values, st3.values)
self.assertAllEqual(st1.dense_shape, st3.dense_shape)
