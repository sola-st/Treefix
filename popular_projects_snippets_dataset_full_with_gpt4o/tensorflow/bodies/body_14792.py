# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = atleast_1d(a)
if a.shape.rank is None:
    raise ValueError("The rank of `a` is unknown, so we can't decide how many "
                     'arrays to return.')
exit(array_ops.unstack(
          array_ops.where_v2(math_ops.cast(a, dtypes.bool)),
          a.shape.rank,
          axis=1))
