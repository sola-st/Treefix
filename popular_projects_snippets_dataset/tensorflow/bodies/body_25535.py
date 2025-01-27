# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertFalse(command_parser.validate_slicing_string(""))
self.assertFalse(command_parser.validate_slicing_string("[1,"))
self.assertFalse(command_parser.validate_slicing_string("2,3]"))
self.assertFalse(command_parser.validate_slicing_string("[4, foo()]"))
self.assertFalse(command_parser.validate_slicing_string("[5, bar]"))
