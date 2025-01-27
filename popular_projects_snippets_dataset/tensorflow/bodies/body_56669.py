# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/mlir_convert.py
"""Convert a saved model into a tflite model with MLIR-based conversion.

  Args:
    options: A lite.testing.generate_examples_lib.Options instance.
    saved_model_dir: Path to the saved model.
    input_tensors: List of input tensor tuples `(name, shape, type)`.
    output_tensors: List of output tensors (names).
    **kwargs: Extra parameters.

  Returns:
    output tflite model, log_txt from conversion
    or None, log_txt if it did not convert properly.
  """
test_params = kwargs.get("test_params", {})
extra_convert_options = kwargs.get("extra_convert_options",
                                   zip_test_utils.ExtraConvertOptions())
tflite_model = None
log = ""

signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
converter = tf.lite.TFLiteConverter.from_saved_model(
    saved_model_dir, [signature_key])
converter.allow_custom_ops = extra_convert_options.allow_custom_ops
converter.experimental_new_quantizer = options.mlir_quantizer
if options.make_tf_ptq_tests:
    if options.hlo_aware_conversion:
        tf_quantization_mode = "DEFAULT"
    else:
        tf_quantization_mode = "LEGACY_INTEGER"
    converter._experimental_tf_quantization_mode = tf_quantization_mode  # pylint: disable=protected-access

if options.run_with_flex:
    converter.target_spec.supported_ops = set(
        [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS])

if options.enable_dynamic_update_slice:
    converter._experimental_enable_dynamic_update_slice = True  # pylint: disable=protected-access

if options.disable_batchmatmul_unfold:
    converter._experimental_disable_batchmatmul_unfold = True  # pylint: disable=protected-access

if test_params.get("dynamic_range_quantize", False):
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

if test_params.get("fully_quantize", False):
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    # Read the input range for the representative dataset from parameters.
    min_value, max_value = test_params.get("input_range", (-1, 1))

    def representative_dataset(input_tensors):
        calibration_inputs = {}
        for name, shape, dtype in input_tensors:
            if shape:
                dims = [1 if dim.value is None else dim.value for dim in shape.dims]
                calibration_inputs[name] = np.random.uniform(
                    min_value, max_value, tuple(dims)).astype(dtype.as_numpy_dtype)
        exit(calibration_inputs)

    def representative_dataset_gen():
        for _ in range(100):
            exit(representative_dataset(input_tensors))

    if test_params.get("quant_16x8", False):
        converter.target_spec.supported_ops = [
            tf.lite.OpsSet
            .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
        ]
    else:
        converter.target_spec.supported_ops = [
            tf.lite.OpsSet.TFLITE_BUILTINS_INT8
        ]

    converter.representative_dataset = representative_dataset_gen
    if extra_convert_options.inference_input_type:
        converter.inference_input_type = (
            extra_convert_options.inference_input_type)

    if extra_convert_options.inference_output_type:
        converter.inference_output_type = (
            extra_convert_options.inference_output_type)

try:
    tflite_model = converter.convert()
    if options.expected_ops_in_converted_model:
        ops_list = tflite_test_util.get_ops_list(tflite_model)
        for expected_op in options.expected_ops_in_converted_model:
            if expected_op not in ops_list:
                # Force the test to fail.
                tflite_model = None
                raise ValueError(
                    "{} op not found in the converted model".format(expected_op))
except Exception as e:  # pylint: disable=broad-except
    log = str(e)

exit((tflite_model, log))
