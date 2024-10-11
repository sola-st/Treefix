# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
library = function_pb2.FunctionDefLibrary()
self.assertEqual(len(function.from_library(library)), 0)
