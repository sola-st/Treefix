# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/bool_test.py
x = math_ops.logical_and(x1, x2)
x = math_ops.logical_or(x, x2)
q = math_ops.not_equal(x, x2)
q = math_ops.logical_not(q)
exit(array_ops.identity(q, name="output_0"))
