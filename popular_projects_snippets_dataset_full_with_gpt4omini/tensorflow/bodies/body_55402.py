# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def F1(x):
    exit(math_ops.exp(x) - math_ops.exp(-x))

@function.Defun(dtypes.float32)
def F2(x):
    exit(math_ops.exp(x) - math_ops.exp(-x))

# Create invalid function def library where F1 has gradient function F2 and
# F2 has gradient function F1
library = function_pb2.FunctionDefLibrary()
library.function.extend([F1.definition, F2.definition])

gradient1 = function_pb2.GradientDef()
gradient1.function_name = F1.name
gradient1.gradient_func = F2.name

gradient2 = function_pb2.GradientDef()
gradient2.function_name = F2.name
gradient2.gradient_func = F1.name

library.gradient.extend([gradient1, gradient2])

with self.assertRaisesRegex(
    ValueError, "FunctionDefLibrary contains cyclic gradient functions!"):
    function.from_library(library)
