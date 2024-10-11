# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that uses functionality that does not work
# with eager tensors (namely build_tensor_info).
with ops.Graph().as_default():
    x = array_ops.placeholder(dtypes.float32, 1, name="x")
    x_tensor_info = utils.build_tensor_info(x)
    inputs = {}
    inputs["foo-input"] = x_tensor_info

    y = array_ops.placeholder(dtypes.float32, name="y")
    y_tensor_info = utils.build_tensor_info(y)
    outputs = {}
    outputs["foo-output"] = y_tensor_info

signature_def = signature_def_utils_impl.build_signature_def(
    inputs, outputs, "foo-method-name")
self.assertEqual("foo-method-name", signature_def.method_name)

# Check inputs in signature def.
self.assertEqual(1, len(signature_def.inputs))
x_tensor_info_actual = signature_def.inputs["foo-input"]
self.assertEqual("x:0", x_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_FLOAT, x_tensor_info_actual.dtype)
self.assertEqual(1, len(x_tensor_info_actual.tensor_shape.dim))
self.assertEqual(1, x_tensor_info_actual.tensor_shape.dim[0].size)

# Check outputs in signature def.
self.assertEqual(1, len(signature_def.outputs))
y_tensor_info_actual = signature_def.outputs["foo-output"]
self.assertEqual("y:0", y_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_FLOAT, y_tensor_info_actual.dtype)
self.assertEqual(0, len(y_tensor_info_actual.tensor_shape.dim))
