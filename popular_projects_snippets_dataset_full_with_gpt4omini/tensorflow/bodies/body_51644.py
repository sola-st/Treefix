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
    metrics_val = constant_op.constant(100, name="metrics_val")
    metrics = {
        "metrics/value":
            metrics_val,
        "metrics/update_op":
            array_ops.identity(metrics_val, name="metrics_op"),
    }

    with self.assertRaises(ValueError):
        signature_def = fn_to_test({},
                                   loss=loss,
                                   predictions=predictions,
                                   metrics=metrics)

    signature_def = fn_to_test(inputs, loss=loss)
    self.assertEqual(method_name, signature_def.method_name)
    self.assertEqual(1, len(signature_def.outputs))

    signature_def = fn_to_test(inputs, metrics=metrics, loss=loss)
    self.assertEqual(method_name, signature_def.method_name)
    self.assertEqual(3, len(signature_def.outputs))
