# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that uses functionality that does not work
# with eager tensors (namely build_tensor_info).
with ops.Graph().as_default():
    input1 = constant_op.constant("a", name="input-1")
    output1 = constant_op.constant("b", name="output-1")
    output2 = constant_op.constant(3.3, name="output-2")
    signature_def = signature_def_utils_impl.classification_signature_def(
        input1, output1, output2)

self.assertEqual(signature_constants.CLASSIFY_METHOD_NAME,
                 signature_def.method_name)

# Check inputs in signature def.
self.assertEqual(1, len(signature_def.inputs))
x_tensor_info_actual = (
    signature_def.inputs[signature_constants.CLASSIFY_INPUTS])
self.assertEqual("input-1:0", x_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_STRING, x_tensor_info_actual.dtype)
self.assertEqual(0, len(x_tensor_info_actual.tensor_shape.dim))

# Check outputs in signature def.
self.assertEqual(2, len(signature_def.outputs))
classes_tensor_info_actual = (
    signature_def.outputs[signature_constants.CLASSIFY_OUTPUT_CLASSES])
self.assertEqual("output-1:0", classes_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_STRING, classes_tensor_info_actual.dtype)
self.assertEqual(0, len(classes_tensor_info_actual.tensor_shape.dim))
scores_tensor_info_actual = (
    signature_def.outputs[signature_constants.CLASSIFY_OUTPUT_SCORES])
self.assertEqual("output-2:0", scores_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_FLOAT, scores_tensor_info_actual.dtype)
self.assertEqual(0, len(scores_tensor_info_actual.tensor_shape.dim))
