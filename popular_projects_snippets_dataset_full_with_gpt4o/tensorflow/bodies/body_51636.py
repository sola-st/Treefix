# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that uses functionality that does not work
# with eager tensors (namely build_tensor_info).
with ops.Graph().as_default():
    input1 = constant_op.constant("a", name="input-1")
    output1 = constant_op.constant(2.2, name="output-1")
    signature_def = signature_def_utils_impl.regression_signature_def(
        input1, output1)

self.assertEqual(signature_constants.REGRESS_METHOD_NAME,
                 signature_def.method_name)

# Check inputs in signature def.
self.assertEqual(1, len(signature_def.inputs))
x_tensor_info_actual = (
    signature_def.inputs[signature_constants.REGRESS_INPUTS])
self.assertEqual("input-1:0", x_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_STRING, x_tensor_info_actual.dtype)
self.assertEqual(0, len(x_tensor_info_actual.tensor_shape.dim))

# Check outputs in signature def.
self.assertEqual(1, len(signature_def.outputs))
y_tensor_info_actual = (
    signature_def.outputs[signature_constants.REGRESS_OUTPUTS])
self.assertEqual("output-1:0", y_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_FLOAT, y_tensor_info_actual.dtype)
self.assertEqual(0, len(y_tensor_info_actual.tensor_shape.dim))
