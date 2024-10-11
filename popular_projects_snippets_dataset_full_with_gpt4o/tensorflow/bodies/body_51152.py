# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that depends on graph-only functions such
# as build_tensor_info.
with ops.Graph().as_default():
    receiver_tensor = array_ops.placeholder(dtypes.string)

    receiver_tensors_alternative_1 = {
        "foo": array_ops.placeholder(dtypes.int64),
        "bar": array_ops.sparse_placeholder(dtypes.float32)
    }

    unfed_input = array_ops.placeholder(dtypes.bool)
    receiver_tensors_alternative_2 = {"unfed": unfed_input}

    receiver_tensors_alternatives = {
        "other": receiver_tensors_alternative_1,
        "with_unfed_input": receiver_tensors_alternative_2
    }

    output_1 = constant_op.constant([1.])
    output_2 = constant_op.constant(["2"])
    output_3 = constant_op.constant(["3"])
    output_4 = unfed_input
    output_5 = math_ops.logical_not(unfed_input)
    export_outputs = {
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
            export_output.RegressionOutput(value=output_1),
        "head-2":
            export_output.ClassificationOutput(classes=output_2),
        "head-3":
            export_output.PredictOutput(outputs={"some_output_3": output_3}),
        "head-4":
            export_output.PredictOutput(outputs={"some_output_4": output_4}),
        "head-5":
            export_output.PredictOutput(outputs={"some_output_5": output_5}),
    }

    signature_defs = export_utils.build_all_signature_defs(
        receiver_tensor, export_outputs, receiver_tensors_alternatives)

    expected_signature_defs = {
        "serving_default":
            signature_def_utils.regression_signature_def(
                receiver_tensor, output_1),
        "head-2":
            signature_def_utils.classification_signature_def(
                receiver_tensor, output_2, None),
        "head-3":
            signature_def_utils.predict_signature_def(
                {"input": receiver_tensor}, {"some_output_3": output_3}),
        "other:head-3":
            signature_def_utils.predict_signature_def(
                receiver_tensors_alternative_1, {"some_output_3": output_3}),

        # Note that the alternatives 'other:serving_default' and
        # 'other:head-2' are invalid, because regression and classification
        # signatures must take a single string input.  Here we verify that
        # these invalid signatures are not included in the export_utils.

        # Similarly, we verify that 'head-4' and 'head-5', which depend on an
        # input that is not being fed as a receiver tensor, are also omitted.

        # All the three heads are present when that input is fed, however:
        "with_unfed_input:head-3":
            signature_def_utils.predict_signature_def(
                receiver_tensors_alternative_2, {"some_output_3": output_3}),
        "with_unfed_input:head-4":
            signature_def_utils.predict_signature_def(
                receiver_tensors_alternative_2, {"some_output_4": output_4}),
        "with_unfed_input:head-5":
            signature_def_utils.predict_signature_def(
                receiver_tensors_alternative_2, {"some_output_5": output_5})
    }

    self.assertDictEqual(expected_signature_defs, signature_defs)
