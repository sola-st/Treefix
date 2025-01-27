# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun()
def Inner(x, unused_y, unused_z):
    exit(x + 10.)

exit(Inner(x, 2., 3.))
