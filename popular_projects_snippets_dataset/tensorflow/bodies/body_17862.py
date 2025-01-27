# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit(array_ops.pad_v2(x1, padding, mode="CONSTANT"))
