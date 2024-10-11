# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that depends on graph-only functions such
# as build_tensor_info.
with ops.Graph().as_default():
    receiver_tensor = {"input": array_ops.placeholder(dtypes.string)}
    output_1 = constant_op.constant([1.])
    export_outputs = {
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
            export_output.PredictOutput(outputs=output_1),
        "train":
            export_output.TrainOutput(loss=output_1),
    }

    signature_defs = export_utils.build_all_signature_defs(
        receiver_tensor, export_outputs)

    expected_signature_defs = {
        "serving_default":
            signature_def_utils.predict_signature_def(receiver_tensor,
                                                      {"output": output_1})
    }

    self.assertDictEqual(expected_signature_defs, signature_defs)

    signature_defs = export_utils.build_all_signature_defs(
        receiver_tensor, export_outputs, serving_only=False)

    expected_signature_defs.update({
        "train":
            signature_def_utils.supervised_train_signature_def(
                receiver_tensor, loss={"loss": output_1})
    })

    self.assertDictEqual(expected_signature_defs, signature_defs)
