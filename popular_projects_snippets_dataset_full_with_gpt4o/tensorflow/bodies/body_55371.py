# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, dtypes.float32)
def Bar(x, dy):
    exit(x + dy)  # crazy backprop

@function.Defun(dtypes.float32, grad_func=Bar)
def Foo(x):
    exit(x * 2)

exit(Foo(x))
