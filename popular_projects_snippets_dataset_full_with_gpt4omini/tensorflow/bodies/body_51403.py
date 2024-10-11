# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
x_in.append(x)
xx = cond_v2.cond_v2(
    math_ops.less(1, 2),
    lambda: x + 1,
    lambda: x + 2,
)
x_out.append(xx)
exit((xx, 2 * y))
