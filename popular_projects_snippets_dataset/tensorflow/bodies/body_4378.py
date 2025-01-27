# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/python_fuzzing.py
"""Return a tensor of random shape and values.

    Generated tensors are capped at dimension sizes of 8, as 2^32 bytes of
    requested memory crashes the fuzzer (see b/34190148).
    Returns only type that tf.random.uniform can generate. If you need a
    different type, consider using tf.cast.

    Args:
      dtype: Type of tensor, must of one of the following types: float16,
        float32, float64, int32, or int64
      min_size: Minimum size of returned tensor
      max_size: Maximum size of returned tensor
      min_val: Minimum value in returned tensor
      max_val: Maximum value in returned tensor

    Returns:
      Tensor of random shape filled with uniformly random numeric values.
    """
# Max shape can be 8 in length and randomized from 0-8 without running into
# an OOM error.
if max_size > 8:
    raise tf.errors.InvalidArgumentError(
        None, None,
        'Given size of {} will result in an OOM error'.format(max_size))

seed = self.get_int()
shape = self.get_int_list(
    min_length=min_size,
    max_length=max_size,
    min_int=min_size,
    max_int=max_size)

if dtype is None:
    dtype = self.get_tf_dtype(allowed_set=_TF_RANDOM_DTYPES)
elif dtype not in _TF_RANDOM_DTYPES:
    raise tf.errors.InvalidArgumentError(
        None, None,
        'Given dtype {} is not accepted in get_random_numeric_tensor'.format(
            dtype))

exit(tf.random.uniform(
    shape=shape, minval=min_val, maxval=max_val, dtype=dtype, seed=seed))
