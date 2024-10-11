# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that uses functionality that does not work
# with eager tensors (namely build_tensor_info).
with ops.Graph().as_default():
    inputs = {
        "input-1": constant_op.constant("a", name="input-1"),
        "input-2": constant_op.constant("b", name="input-2"),
    }
    loss = {"loss-1": constant_op.constant(0.45, name="loss-1")}
    predictions = {
        "classes": constant_op.constant([100], name="classes"),
    }
    metrics_val = constant_op.constant(100.0, name="metrics_val")
    metrics = {
        "metrics/value":
            metrics_val,
        "metrics/update_op":
            array_ops.identity(metrics_val, name="metrics_op"),
    }

    signature_def = fn_to_test(inputs, loss, predictions, metrics)

self.assertEqual(method_name, signature_def.method_name)

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
self.assertEqual(4, len(signature_def.outputs))
self.assertEqual("loss-1:0", signature_def.outputs["loss-1"].name)
self.assertEqual(types_pb2.DT_FLOAT, signature_def.outputs["loss-1"].dtype)

self.assertEqual("classes:0", signature_def.outputs["classes"].name)
self.assertEqual(1, len(signature_def.outputs["classes"].tensor_shape.dim))

self.assertEqual(
    "metrics_val:0", signature_def.outputs["metrics/value"].name)
self.assertEqual(
    types_pb2.DT_FLOAT, signature_def.outputs["metrics/value"].dtype)

self.assertEqual(
    "metrics_op:0", signature_def.outputs["metrics/update_op"].name)
self.assertEqual(
    types_pb2.DT_FLOAT, signature_def.outputs["metrics/value"].dtype)
