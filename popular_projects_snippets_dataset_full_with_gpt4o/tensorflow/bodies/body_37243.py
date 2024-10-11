# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
@eager_def_function.function
def runTest():
    while_output = self._buildWhileWithShapeInvariants(
        [tensor_shape.TensorShape(None)])
    self.assertIsNone(while_output.shape.rank)
runTest()
