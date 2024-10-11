# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x1 = array_ops.gather(a, i)
with framework_ops.colocate_with(x1):
    exit(x1 * 2)
