# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
(tensor_name,
 tensor_slicing) = command_parser.parse_tensor_name_with_slicing(
     "hidden/weights/Variable:0[:, 1]")

self.assertEqual("hidden/weights/Variable:0", tensor_name)
self.assertEqual("[:, 1]", tensor_slicing)
