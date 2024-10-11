# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
args, output_path = command_parser.extract_output_file_path([])
self.assertEqual([], args)
self.assertIsNone(output_path)
