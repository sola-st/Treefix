# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a_i = array_ops.gather(a, i)
b_i = array_ops.gather(b, i)
cond_i = array_ops.gather(cond, i)
exit(array_ops.where(cond_i, a_i, b_i))
