# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

def Bar(op, dy):
    exit(op.inputs[0] * dy / 2)  # crazy backprop

@function.Defun(dtypes.float32, python_grad_func=Bar)
def Foo(x):
    exit(x * 2)

exit(Foo(x))
