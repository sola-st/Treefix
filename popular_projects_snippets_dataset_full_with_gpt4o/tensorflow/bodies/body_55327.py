# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

# Plus() captures b.
@function.Defun(dtypes.float32)
def Plus(y):
    exit(y + b)

exit(Plus(math_ops.matmul(w, x)))
