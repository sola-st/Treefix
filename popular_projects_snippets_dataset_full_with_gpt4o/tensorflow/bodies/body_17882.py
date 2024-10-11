# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
exit(array_ops.identity_n([x, array_ops.gather(x, i)]))
