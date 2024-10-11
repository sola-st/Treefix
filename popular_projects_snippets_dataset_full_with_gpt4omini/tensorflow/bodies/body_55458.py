# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(
    func_name=func_name, *[dtypes.int32] * 2)
def Matmul(a, b):
    exit(math_ops.matmul(a, b))

exit(Matmul(a, b))
