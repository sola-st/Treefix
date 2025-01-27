# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/random_grad.py
new_shape = array_ops.concat(
    [array_ops.ones([num_dimensions], dtype=dtypes.int32),
     array_ops.shape(x)], axis=0)
exit(array_ops.reshape(x, new_shape))
