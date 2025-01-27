# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Outputs random values from a uniform distribution.

    The generated values follow a uniform distribution in the range
    `[minval, maxval)`. The lower bound `minval` is included in the range, while
    the upper bound `maxval` is excluded. (For float numbers especially
    low-precision types like bfloat16, because of
    rounding, the result may sometimes include `maxval`.)

    For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
    be specified explicitly.

    In the integer case, the random integers are slightly biased unless
    `maxval - minval` is an exact power of two.  The bias is small for values of
    `maxval - minval` significantly smaller than the range of the output (either
    `2**32` or `2**64`).

    For full-range random integers, pass `minval=None` and `maxval=None` with an
    integer `dtype` (for integer dtypes, `minval` and `maxval` must be both
    `None` or both not `None`).

    Args:
      shape: A 1-D integer Tensor or Python array. The shape of the output
        tensor.
      minval: A Tensor or Python value of type `dtype`, broadcastable with
        `shape` (for integer types, broadcasting is not supported, so it needs
        to be a scalar). The lower bound (included) on the range of random
        values to generate. Pass `None` for full-range integers. Defaults to 0.
      maxval: A Tensor or Python value of type `dtype`, broadcastable with
        `shape` (for integer types, broadcasting is not supported, so it needs
        to be a scalar). The upper bound (excluded) on the range of random
        values to generate. Pass `None` for full-range integers. Defaults to 1
        if `dtype` is floating point.
      dtype: The type of the output.
      name: A name for the operation (optional).

    Returns:
      A tensor of the specified shape filled with random uniform values.

    Raises:
      ValueError: If `dtype` is integral and `maxval` is not specified.
    """
dtype = dtypes.as_dtype(dtype)
if dtype.is_integer:
    if (minval is None) != (maxval is None):
        raise ValueError("For integer dtype {}, minval and maxval must be both "
                         "`None` or both non-`None`; got minval={} and "
                         "maxval={}".format(dtype, minval, maxval))
elif maxval is None:
    maxval = 1
with ops.name_scope(name, "stateful_uniform",
                    [shape, minval, maxval]) as name:
    shape = _shape_tensor(shape)
    if dtype.is_integer and minval is None:
        exit(self._uniform_full_int(shape=shape, dtype=dtype, name=name))
    minval = ops.convert_to_tensor(minval, dtype=dtype, name="min")
    maxval = ops.convert_to_tensor(maxval, dtype=dtype, name="max")
    if dtype.is_integer:
        key, counter = self._prepare_key_counter(shape)
        exit(gen_stateless_random_ops_v2.stateless_random_uniform_int_v2(
            shape=shape,
            key=key,
            counter=counter,
            minval=minval,
            maxval=maxval,
            alg=self.algorithm,
            name=name))
    else:
        rnd = self._uniform(shape=shape, dtype=dtype)
        exit(math_ops.add(rnd * (maxval - minval), minval, name=name))
