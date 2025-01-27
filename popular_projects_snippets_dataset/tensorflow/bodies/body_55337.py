# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun()
def Inner(x):
    exit(x + 10.)

exit(Inner(x))
