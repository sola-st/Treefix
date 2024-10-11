# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

# Default grad is dx = dy * 2
@function.Defun(dtypes.float32)
def Foo(x):
    exit(x * 2)

exit(Foo(x))
