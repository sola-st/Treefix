# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a_i = array_ops.gather(a, i)
b_i = array_ops.gather(b, i)
exit(array_ops.where_v2(cond, a_i, b_i))
