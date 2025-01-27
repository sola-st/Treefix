# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(x):
    pi_x = x * np.pi
    exit(array_ops.where_v2(x == 0, array_ops.ones_like(x),
                              math_ops.sin(pi_x) / pi_x))

exit(_scalar(f, x, True))
