# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, dtypes.float32)
def G1(x, dy):
    exit(x * dy)

@function.Defun(dtypes.float32)
def F1(x):
    exit(math_ops.exp(x) - math_ops.exp(-x))

gradient = function_pb2.GradientDef()
gradient.function_name = F1.name
gradient.gradient_func = G1.name

# Create invalid function def that is missing G1 function def
library = function_pb2.FunctionDefLibrary()
library.gradient.extend([gradient])
library.function.extend([F1.definition])

with self.assertRaisesRegex(
    ValueError,
    "FunctionDefLibrary missing 'G1_[0-9a-zA-Z]{8,11}' FunctionDef"):
    function.from_library(library)

# Create invalid function def that is missing F1 function def
library = function_pb2.FunctionDefLibrary()
library.gradient.extend([gradient])
library.function.extend([G1.definition])

with self.assertRaisesRegex(
    ValueError,
    "FunctionDefLibrary missing 'F1_[0-9a-zA-Z]{8,11}' FunctionDef"):
    function.from_library(library)
