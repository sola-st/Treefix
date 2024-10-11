# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a = array_ops.gather(x, i) if stack_a else x
b = array_ops.gather(y, i) if stack_b else y
exit(math_ops.matmul(a, b, transpose_a=tr_a, transpose_b=tr_b))
