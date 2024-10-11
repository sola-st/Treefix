# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def Cube(x):
    exit(x * x * x)

exit(Cube(x) + y)
