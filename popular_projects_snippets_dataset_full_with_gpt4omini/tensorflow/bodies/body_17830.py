# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x_i = array_ops.gather(x, i)
exit((array_ops.size(x_i), array_ops.size(x_i, out_type=dtypes.int64)))
