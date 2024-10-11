# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
minval = ops.convert_to_tensor(minval)
exit(random_ops.random_uniform(
    dims, minval, maxval, dtype=minval.dtype, name=name))
