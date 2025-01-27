# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x_i = array_ops.gather(x, i)
y_i = array_ops.gather(y, i)
x_0 = array_ops.gather(x, 0)
exit((math_ops.cross(x_i, y_i), math_ops.cross(x_0, y_i)))
