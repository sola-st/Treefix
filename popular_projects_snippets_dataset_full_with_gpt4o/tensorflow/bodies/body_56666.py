# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples.py
options = generate_examples_lib.Options()

options.output_path = FLAGS.output_path
options.zip_to_output = FLAGS.zip_to_output
options.known_bugs_are_errors = FLAGS.known_bugs_are_errors
options.ignore_converter_errors = FLAGS.ignore_converter_errors
options.save_graphdefs = FLAGS.save_graphdefs
options.run_with_flex = FLAGS.run_with_flex
options.make_edgetpu_tests = FLAGS.make_edgetpu_tests
options.make_tf_ptq_tests = FLAGS.make_tf_ptq_tests
options.tflite_convert_function = mlir_convert.mlir_convert
options.known_bugs = MLIR_CONVERTER_KNOWN_BUGS
options.make_forward_compat_test = FLAGS.make_forward_compat_test
options.no_tests_limit = FLAGS.no_tests_limit
options.mlir_quantizer = FLAGS.mlir_quantizer
options.skip_high_dimension_inputs = FLAGS.skip_high_dimension_inputs

if FLAGS.test_sets:
    test_sets = FLAGS.test_sets.split(",")
    generate_examples_lib.generate_multi_set_examples(options, test_sets)
else:
    generate_examples_lib.generate_examples(options)
