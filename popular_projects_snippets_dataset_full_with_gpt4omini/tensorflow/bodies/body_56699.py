# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Build the model with parameter values set in param_dict_real.

        Args:
          label: Label of the model
          param_dict_real: Parameter dictionary (arguments to the factories
            make_graph and make_test_inputs)
          zip_path_label: Filename in the zip

        Returns:
          (tflite_model_binary, report) where tflite_model_binary is the
          serialized flatbuffer as a string and report is a dictionary with
          keys `tflite_converter_log` (log of conversion), `tf_log` (log of tf
          conversion), `converter` (a string of success status of the
          conversion), `tf` (a string success status of the conversion).
        """

np.random.seed(RANDOM_SEED)
report = {
    "tflite_converter": report_lib.NOTRUN,
    "tf": report_lib.FAILED
}

# Build graph
report["tf_log"] = ""
report["tflite_converter_log"] = ""
tf.compat.v1.reset_default_graph()

with tf.Graph().as_default():
    with tf.device("/cpu:0"):
        try:
            inputs, outputs = make_graph(param_dict_real)
            inputs = [x for x in inputs if x is not None]
        except (tf.errors.UnimplementedError,
                tf.errors.InvalidArgumentError, ValueError):
            report["tf_log"] += traceback.format_exc()
            exit((None, report))

    sess = tf.compat.v1.Session()
    try:
        baseline_inputs, baseline_outputs = (
            make_test_inputs(param_dict_real, sess, inputs, outputs))
        baseline_inputs = [x for x in baseline_inputs if x is not None]
        # Converts baseline inputs/outputs to maps. The signature input and
        # output names are set to be the same as the tensor names.
        input_names = [_normalize_input_name(x.name) for x in inputs]
        output_names = [_normalize_output_name(x.name) for x in outputs]
        baseline_input_map = dict(zip(input_names, baseline_inputs))
        baseline_output_map = dict(zip(output_names, baseline_outputs))
    except (tf.errors.UnimplementedError, tf.errors.InvalidArgumentError,
            ValueError):
        report["tf_log"] += traceback.format_exc()
        exit((None, report))
    report["tflite_converter"] = report_lib.FAILED
    report["tf"] = report_lib.SUCCESS

    # Builds a saved model with the default signature key.
    input_names, tensor_info_inputs = _get_tensor_info(
        inputs, "input_", _normalize_input_name)
    output_tensors, tensor_info_outputs = _get_tensor_info(
        outputs, "output_", _normalize_output_name)
    input_tensors = [
        (name, t.shape, t.dtype) for name, t in zip(input_names, inputs)
    ]

    inference_signature = (
        tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
            inputs=tensor_info_inputs,
            outputs=tensor_info_outputs,
            method_name="op_test"))
    saved_model_dir = tempfile.mkdtemp("op_test")
    saved_model_tags = [tf.saved_model.SERVING]
    signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
    builder = tf.compat.v1.saved_model.builder.SavedModelBuilder(
        saved_model_dir)
    builder.add_meta_graph_and_variables(
        sess,
        saved_model_tags,
        signature_def_map={
            signature_key: inference_signature,
        },
        strip_default_attrs=True)
    builder.save(as_text=False)
    # pylint: disable=g-long-ternary
    graph_def = freeze_graph(
        sess,
        tf.compat.v1.global_variables() + inputs +
        outputs) if use_frozen_graph else sess.graph_def

if "split_tflite_lstm_inputs" in param_dict_real:
    extra_convert_options.split_tflite_lstm_inputs = param_dict_real[
        "split_tflite_lstm_inputs"]
tflite_model_binary, converter_log = options.tflite_convert_function(
    options,
    saved_model_dir,
    input_tensors,
    output_tensors,
    extra_convert_options=extra_convert_options,
    test_params=param_dict_real)
report["tflite_converter"] = (
    report_lib.SUCCESS
    if tflite_model_binary is not None else report_lib.FAILED)
report["tflite_converter_log"] = converter_log

if options.save_graphdefs:
    zipinfo = zipfile.ZipInfo(zip_path_label + ".pbtxt")
    archive.writestr(zipinfo, text_format.MessageToString(graph_def),
                     zipfile.ZIP_DEFLATED)

if tflite_model_binary:
    if options.make_edgetpu_tests:
        # Set proper min max values according to input dtype.
        baseline_input_map, baseline_output_map = generate_inputs_outputs(
            tflite_model_binary, min_value=0, max_value=255)
    zipinfo = zipfile.ZipInfo(zip_path_label + ".bin")
    archive.writestr(zipinfo, tflite_model_binary, zipfile.ZIP_DEFLATED)

    example = {
        "inputs": baseline_input_map,
        "outputs": baseline_output_map
    }

    example_fp = io.StringIO()
    write_examples(example_fp, [example])
    zipinfo = zipfile.ZipInfo(zip_path_label + ".inputs")
    archive.writestr(zipinfo, example_fp.getvalue(), zipfile.ZIP_DEFLATED)

    example_fp2 = io.StringIO()
    write_test_cases(example_fp2, zip_path_label + ".bin", [example])
    zipinfo = zipfile.ZipInfo(zip_path_label + "_tests.txt")
    archive.writestr(zipinfo, example_fp2.getvalue(),
                     zipfile.ZIP_DEFLATED)

    zip_manifest_label = zip_path_label + " " + label
    if zip_path_label == label:
        zip_manifest_label = zip_path_label

    zip_manifest.append(zip_manifest_label + "\n")

exit((tflite_model_binary, report))
