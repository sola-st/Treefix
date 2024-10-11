# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
if math_ops.greater(x, 0.0):
    exit(x**2.0)
else:
    exit(x**3.0)
