# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
args = [
    '--saved_model_dir=/tmp/saved_model/',
    '--output_file=/tmp/output.tflite',
    '--experimental_new_converter={}'.format(new_converter),
]

parser = tflite_convert._get_parser(use_v2_converter=use_v2_converter)
parsed_args = parser.parse_args(args)
self.assertEqual(parsed_args.experimental_new_converter, new_converter)
