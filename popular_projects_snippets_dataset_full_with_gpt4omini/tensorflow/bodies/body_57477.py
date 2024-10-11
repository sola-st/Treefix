# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
args = [
    '--saved_model_dir=/tmp/saved_model/',
    '--output_file=/tmp/output.tflite',
]

# Note that when the flag parses to None, the converter uses the default
# value, which is True.

parser = tflite_convert._get_parser(use_v2_converter=use_v2_converter)
parsed_args = parser.parse_args(args)
self.assertTrue(parsed_args.experimental_new_converter)
self.assertIsNone(parsed_args.experimental_new_quantizer)
