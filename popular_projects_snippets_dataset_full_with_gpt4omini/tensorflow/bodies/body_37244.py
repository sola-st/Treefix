# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
while_output = self._buildWhileWithShapeInvariants(
    [tensor_shape.TensorShape([None])])
self.assertAllEqual(while_output.shape.as_list(), [None])
