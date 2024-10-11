# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_lib.py
# Directory where the outputs will be go.
self.output_path = None
# Particular zip to output.
self.zip_to_output = None
# If a particular model is affected by a known bug count it as a converter
# error.
self.known_bugs_are_errors = False
# Raise an exception if any converter error is encountered.
self.ignore_converter_errors = False
# Include intermediate graphdefs in the output zip files.
self.save_graphdefs = False
# Whether the TFLite Flex converter is being used.
self.run_with_flex = False
# Whether to generate test cases for edgetpu.
self.make_edgetpu_tests = False
# Whether to generate test cases for TF PTQ.
self.make_tf_ptq_tests = False
# For TF Quantization only: where conversion for HLO target.
self.hlo_aware_conversion = True
# The function to convert a TensorFLow model to TFLite model.
# See the document for `mlir_convert` function for its required signature.
self.tflite_convert_function = None
# A map from regular expression to bug number. Any test failure with label
# matching the expression will be considered due to the corresponding bug.
self.known_bugs = {}
# Make tests by setting TF forward compatibility horizon to the future.
self.make_forward_compat_test = False
# No limitation on the number of tests.
self.no_tests_limit = False
# Do not create conversion report.
self.no_conversion_report = False
# State of multiple test set generation. This stores state values those
# should be kept and updated while generating examples over multiple
# test sets.
# TODO(juhoha): Separate the state from the options.
self.multi_gen_state = None
self.mlir_quantizer = False
# The list of ops' name that should exist in the converted model.
# This feature is currently only supported in MLIR conversion path.
# Example of supported ops' name:
# - "AVERAGE_POOL_2D" for builtin op.
# - "NumericVerify" for custom op.
self.expected_ops_in_converted_model = []
# Whether to skip generating tests with high dimension input shape.
self.skip_high_dimension_inputs = False
# Whether to enable DynamicUpdateSlice op.
self.enable_dynamic_update_slice = False
# Whether to disable unrolling batch matmul.
self.disable_batchmatmul_unfold = False
