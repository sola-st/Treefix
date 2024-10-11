# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, dtypes.float32)
def G(x, dy):
    exit(x * dy)

@function.Defun(dtypes.float32, grad_func=G)
def F(x):
    exit(math_ops.exp(x) - math_ops.exp(-x))

self.expectFunctionsEqual(F, grad_func=G)
