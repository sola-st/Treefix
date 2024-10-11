# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertTrue(command_parser.validate_slicing_string("[1]"))
self.assertTrue(command_parser.validate_slicing_string("[2,3]"))
self.assertTrue(command_parser.validate_slicing_string("[4, 5, 6]"))
self.assertTrue(command_parser.validate_slicing_string("[7,:, :]"))
