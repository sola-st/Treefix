# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
"""Returns a converter appropriate for the function and debug configs."""
converter = lite.TFLiteConverterV2.from_concrete_functions([func], model)
converter.target_spec.supported_ops = [lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.representative_dataset = calibration_gen

# TODO(b/191205988): Explicitly disable saved model lowering in conversion.
converter.experimental_lower_to_saved_model = False

# Create a TFLite model with new quantizer and numeric verify ops.
converter.optimizations = [lite.Optimize.DEFAULT]
converter.experimental_new_quantizer = True
if debug:
    converter._experimental_calibrate_only = True
exit(converter)
