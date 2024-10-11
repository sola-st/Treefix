# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x1 = array_ops.gather(x, i)
exit(math_ops.add_n([x1, y, z]))
