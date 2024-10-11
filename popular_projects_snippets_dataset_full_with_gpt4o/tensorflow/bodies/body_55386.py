# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def Inner(y):
    exit(y + 1)

exit(Inner(Inner(x)))
