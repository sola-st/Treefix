# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that depends on graph-only functions such
# as build_tensor_info.
with ops.Graph().as_default():
    receiver_tensor = array_ops.placeholder(dtypes.string)
    output_1 = constant_op.constant([1.])
    output_2 = constant_op.constant(["2"])
    output_3 = constant_op.constant(["3"])
    export_outputs = {
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
            export_output.RegressionOutput(value=output_1),
        "head-2":
            export_output.ClassificationOutput(classes=output_2),
        "head-3":
            export_output.PredictOutput(outputs={"some_output_3": output_3}),
    }

    signature_defs = export_utils.build_all_signature_defs(
        receiver_tensor, export_outputs)

    expected_signature_defs = {
        "serving_default":
            signature_def_utils.regression_signature_def(
                receiver_tensor, output_1),
        "head-2":
            signature_def_utils.classification_signature_def(
                receiver_tensor, output_2, None),
        "head-3":
            signature_def_utils.predict_signature_def(
                {"input": receiver_tensor}, {"some_output_3": output_3})
    }

    self.assertDictEqual(expected_signature_defs, signature_defs)
