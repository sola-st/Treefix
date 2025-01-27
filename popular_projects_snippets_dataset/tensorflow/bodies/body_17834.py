# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x_i = array_ops.gather(x, i)
y_i = array_ops.gather(y, i)
exit((array_ops.shape_n([x_i, x, y,
                          y_i]), array_ops.shape_n([x_i, x, y, y_i],
                                                   out_type=dtypes.int64)))
