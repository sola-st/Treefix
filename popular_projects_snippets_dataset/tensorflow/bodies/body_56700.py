# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Helper to make a zip file of a bunch of TensorFlow models.

  This does a cartesian product of the dictionary of test_parameters and
  calls make_graph() for each item in the cartesian product set.
  If the graph is built successfully, then make_test_inputs() is called to
  build expected input/output value pairs. The model is then converted to
  tflite, and the examples are serialized with the tflite model into a zip
  file (2 files per item in the cartesian product set).

  Args:
    options: An Options instance.
    test_parameters: Dictionary mapping to lists for each parameter.
      e.g. `{"strides": [[1,3,3,1], [1,2,2,1]], "foo": [1.2, 1.3]}`
    make_graph: function that takes current parameters and returns tuple
      `[input1, input2, ...], [output1, output2, ...]`
    make_test_inputs: function taking `curr_params`, `session`, `input_tensors`,
      `output_tensors` and returns tuple `(input_values, output_values)`.
    extra_convert_options: Additional convert options.
    use_frozen_graph: Whether or not freeze graph before convertion.
    expected_tf_failures: Number of times tensorflow is expected to fail in
      executing the input graphs. In some cases it is OK for TensorFlow to fail
      because the one or more combination of parameters is invalid.

  Raises:
    RuntimeError: if there are converter errors that can't be ignored.
  """
zip_path = os.path.join(options.output_path, options.zip_to_output)
parameter_count = 0
for parameters in test_parameters:
    parameter_count += functools.reduce(
        operator.mul, [len(values) for values in parameters.values()])

all_parameter_count = parameter_count
if options.multi_gen_state:
    all_parameter_count += options.multi_gen_state.parameter_count
if not options.no_tests_limit and all_parameter_count > _MAX_TESTS_PER_ZIP:
    raise RuntimeError(
        "Too many parameter combinations for generating '%s'.\n"
        "There are at least %d combinations while the upper limit is %d.\n"
        "Having too many combinations will slow down the tests.\n"
        "Please consider splitting the test into multiple functions.\n" %
        (zip_path, all_parameter_count, _MAX_TESTS_PER_ZIP))
if options.multi_gen_state:
    options.multi_gen_state.parameter_count = all_parameter_count

# TODO(aselle): Make this allow multiple inputs outputs.
if options.multi_gen_state:
    archive = options.multi_gen_state.archive
else:
    archive = zipfile.PyZipFile(zip_path, "w")
zip_manifest = []
convert_report = []
converter_errors = 0

processed_labels = set()

if options.make_tf_ptq_tests:
    # For cases with fully_quantize is True, also generates a case with
    # fully_quantize is False. Marks these cases as suitable for PTQ tests.
    parameter_count = 0
    for parameters in test_parameters:
        if True in parameters.get("fully_quantize", []):
            parameters.update({"fully_quantize": [True, False], "tf_ptq": [True]})
            # TODO(b/199054047): Support 16x8 quantization in TF Quantization.
            parameters.update({"quant_16x8": [False]})
            parameter_count += functools.reduce(
                operator.mul, [len(values) for values in parameters.values()])

if options.make_edgetpu_tests:
    extra_convert_options.inference_input_type = tf.uint8
    extra_convert_options.inference_output_type = tf.uint8
    # Only count parameters when fully_quantize is True.
    parameter_count = 0
    for parameters in test_parameters:
        if True in parameters.get("fully_quantize",
                                  []) and False in parameters.get(
                                      "quant_16x8", [False]):
            parameter_count += functools.reduce(operator.mul, [
                len(values)
                for key, values in parameters.items()
                if key != "fully_quantize" and key != "quant_16x8"
            ])

label_base_path = zip_path
if options.multi_gen_state:
    label_base_path = options.multi_gen_state.label_base_path

i = 1
for parameters in test_parameters:
    keys = parameters.keys()
    for curr in itertools.product(*parameters.values()):
        label = label_base_path.replace(".zip", "_") + (",".join(
            "%s=%r" % z for z in sorted(zip(keys, curr))).replace(" ", ""))
        if label[0] == "/":
            label = label[1:]

        zip_path_label = label
        if len(os.path.basename(zip_path_label)) > 245:
            zip_path_label = label_base_path.replace(".zip", "_") + str(i)

        i += 1
        if label in processed_labels:
            # Do not populate data for the same label more than once. It will cause
            # errors when unzipping.
            continue
        processed_labels.add(label)

        param_dict = dict(zip(keys, curr))

        if options.make_tf_ptq_tests and not param_dict.get("tf_ptq", False):
            continue

        if options.make_edgetpu_tests and (not param_dict.get(
            "fully_quantize", False) or param_dict.get("quant_16x8", False)):
            continue

        def generate_inputs_outputs(tflite_model_binary,
                                    min_value=0,
                                    max_value=255):
            """Generate input values and output values of the given tflite model.

        Args:
          tflite_model_binary: A serialized flatbuffer as a string.
          min_value: min value for the input tensor.
          max_value: max value for the input tensor.

        Returns:
          (input_values, output_values): Maps of input values and output values
          built.
        """
            interpreter = tf.lite.Interpreter(model_content=tflite_model_binary)
            interpreter.allocate_tensors()

            input_details = interpreter.get_input_details()
            input_values = {}
            for input_detail in input_details:
                input_value = create_tensor_data(
                    input_detail["dtype"],
                    input_detail["shape"],
                    min_value=min_value,
                    max_value=max_value)
                interpreter.set_tensor(input_detail["index"], input_value)
                input_values.update(
                    {_normalize_input_name(input_detail["name"]): input_value})

            interpreter.invoke()

            output_details = interpreter.get_output_details()
            output_values = {}
            for output_detail in output_details:
                output_values.update({
                    _normalize_output_name(output_detail["name"]):
                        interpreter.get_tensor(output_detail["index"])
                })

            exit((input_values, output_values))

        def build_example(label, param_dict_real, zip_path_label):
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

        _, report = build_example(label, param_dict, zip_path_label)

        if report["tflite_converter"] == report_lib.FAILED:
            ignore_error = False
            if not options.known_bugs_are_errors:
                for pattern, bug_number in options.known_bugs.items():
                    if re.search(pattern, label):
                        print("Ignored converter error due to bug %s" % bug_number)
                        ignore_error = True
            if not ignore_error:
                converter_errors += 1
                print("-----------------\nconverter error!\n%s\n-----------------\n" %
                      report["tflite_converter_log"])

        convert_report.append((param_dict, report))

if not options.no_conversion_report:
    report_io = io.StringIO()
    report_lib.make_report_table(report_io, zip_path, convert_report)
    if options.multi_gen_state:
        zipinfo = zipfile.ZipInfo("report_" + options.multi_gen_state.test_name +
                                  ".html")
        archive.writestr(zipinfo, report_io.getvalue())
    else:
        zipinfo = zipfile.ZipInfo("report.html")
        archive.writestr(zipinfo, report_io.getvalue())

if options.multi_gen_state:
    options.multi_gen_state.zip_manifest.extend(zip_manifest)
else:
    zipinfo = zipfile.ZipInfo("manifest.txt")
    archive.writestr(zipinfo, "".join(zip_manifest), zipfile.ZIP_DEFLATED)

# Log statistics of what succeeded
total_conversions = len(convert_report)
tf_success = sum(
    1 for x in convert_report if x[1]["tf"] == report_lib.SUCCESS)
converter_success = sum(1 for x in convert_report
                        if x[1]["tflite_converter"] == report_lib.SUCCESS)
percent = 0
if tf_success > 0:
    percent = float(converter_success) / float(tf_success) * 100.
tf.compat.v1.logging.info(
    ("Archive %s Considered %d graphs, %d TF evaluated graphs "
     " and %d converted graphs (%.1f%%"), zip_path, total_conversions,
    tf_success, converter_success, percent)

tf_failures = parameter_count - tf_success

if tf_failures / parameter_count > 0.8:
    raise RuntimeError(("Test for '%s' is not very useful. "
                        "TensorFlow fails in %d percent of the cases.") %
                       (zip_path, int(100 * tf_failures / parameter_count)))

if tf_failures != expected_tf_failures and not (options.make_edgetpu_tests or
                                                options.make_tf_ptq_tests):
    raise RuntimeError(("Expected TF to fail %d times while generating '%s', "
                        "but that happened %d times") %
                       (expected_tf_failures, zip_path, tf_failures))

if not options.ignore_converter_errors and converter_errors > 0:
    raise RuntimeError("Found %d errors while generating models" %
                       converter_errors)
