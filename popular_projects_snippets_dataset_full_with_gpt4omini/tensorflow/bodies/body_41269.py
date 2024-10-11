# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
exit(math_ops.matmul(t, t))
