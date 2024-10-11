# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that uses functionality that does not work
# with eager tensors (namely build_tensor_info).
with ops.Graph().as_default():
    input1 = constant_op.constant("a", name="input-1")
    input2 = constant_op.constant("b", name="input-2")
    output1 = constant_op.constant("c", name="output-1")
    output2 = constant_op.constant("d", name="output-2")
    signature_def = signature_def_utils_impl.predict_signature_def(
        {
            "input-1": input1,
            "input-2": input2
        }, {
            "output-1": output1,
            "output-2": output2
        })

self.assertEqual(signature_constants.PREDICT_METHOD_NAME,
                 signature_def.method_name)

# Check inputs in signature def.
self.assertEqual(2, len(signature_def.inputs))
input1_tensor_info_actual = (signature_def.inputs["input-1"])
self.assertEqual("input-1:0", input1_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_STRING, input1_tensor_info_actual.dtype)
self.assertEqual(0, len(input1_tensor_info_actual.tensor_shape.dim))
input2_tensor_info_actual = (signature_def.inputs["input-2"])
self.assertEqual("input-2:0", input2_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_STRING, input2_tensor_info_actual.dtype)
self.assertEqual(0, len(input2_tensor_info_actual.tensor_shape.dim))

# Check outputs in signature def.
self.assertEqual(2, len(signature_def.outputs))
output1_tensor_info_actual = (signature_def.outputs["output-1"])
self.assertEqual("output-1:0", output1_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_STRING, output1_tensor_info_actual.dtype)
self.assertEqual(0, len(output1_tensor_info_actual.tensor_shape.dim))
output2_tensor_info_actual = (signature_def.outputs["output-2"])
self.assertEqual("output-2:0", output2_tensor_info_actual.name)
self.assertEqual(types_pb2.DT_STRING, output2_tensor_info_actual.dtype)
self.assertEqual(0, len(output2_tensor_info_actual.tensor_shape.dim))
