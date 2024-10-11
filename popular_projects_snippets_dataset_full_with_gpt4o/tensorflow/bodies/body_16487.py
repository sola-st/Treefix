# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Shared implementation of the various dropout functions.

  Args:
    x: same as the namesake in `dropout_v2`.
    rate: same as the namesake in `dropout_v2`.
    noise_shape: same as the namesake in `dropout_v2`.
    uniform_sampler: a callable of signature `(shape, dtype) ->
      Tensor`, used to generate a tensor of uniformly-distributed
      random numbers in the range `[0, 1)`, of the given shape and dtype.
    dummy_rng_step: a callable of signature `() -> None`, to make a
      dummy RNG call in the fast path. In the fast path where rate is
      0, we don't need to generate random numbers, but some samplers
      still require you to make an RNG call, to make sure that RNG
      states won't depend on whether the fast path is taken.
    name: same as the namesake in `dropout_v2`.
    default_name: a default name in case `name` is `None`.

  Returns:
    A Tensor of the same shape and dtype of `x`.
  """
with ops.name_scope(name, default_name, [x]) as name:
    is_rate_number = isinstance(rate, numbers.Real)
    if is_rate_number and (rate < 0 or rate >= 1):
        raise ValueError("`rate` must be a scalar tensor or a float in the "
                         f"range [0, 1). Received: rate={rate}")
    x = ops.convert_to_tensor(x, name="x")
    x_dtype = x.dtype
    if not x_dtype.is_floating:
        raise ValueError(
            "`x.dtype` must be a floating point tensor as `x` will be "
            f"scaled. Received: x_dtype={x_dtype}")
    if is_rate_number and rate == 0:
        # Fast-path: Return the input immediately if rate is non-tensor & is `0`.
        # We trigger this after all error checking
        # and after `x` has been converted to a tensor, to prevent inconsistent
        # tensor conversions/error raising if rate is changed to/from 0.
        #
        # We also explicitly call `dummy_rng_step` to make sure
        # we don't change the random number generation behavior of
        # stateful random ops by entering a fastpath,
        # despite not generating a random tensor in the fastpath
        dummy_rng_step()
        exit(x)

    is_executing_eagerly = context.executing_eagerly()
    if not tensor_util.is_tf_type(rate):
        if is_rate_number:
            keep_prob = 1 - rate
            scale = 1 / keep_prob
            scale = ops.convert_to_tensor(scale, dtype=x_dtype)
            ret = gen_math_ops.mul(x, scale)
        else:
            raise ValueError(
                f"`rate` must be a scalar or scalar tensor. Received: rate={rate}")
    else:
        rate.get_shape().assert_has_rank(0)
        rate_dtype = rate.dtype
        if rate_dtype != x_dtype:
            if not rate_dtype.is_compatible_with(x_dtype):
                raise ValueError(
                    "`x.dtype` must be compatible with `rate.dtype`. "
                    f"Received: x.dtype={x_dtype} and rate.dtype={rate_dtype}")
            rate = gen_math_ops.cast(rate, x_dtype, name="rate")
        one_tensor = constant_op.constant(1, dtype=x_dtype)
        ret = gen_math_ops.real_div(x, gen_math_ops.sub(one_tensor, rate))

    noise_shape = _get_noise_shape(x, noise_shape)
    # Sample a uniform distribution on [0.0, 1.0) and select values larger
    # than or equal to `rate`.
    random_tensor = uniform_sampler(shape=noise_shape, dtype=x_dtype)
    keep_mask = random_tensor >= rate
    zero_tensor = constant_op.constant(0, dtype=x_dtype)
    ret = array_ops.where_v2(keep_mask, ret, zero_tensor)
    if not is_executing_eagerly:
        ret.set_shape(x.get_shape())
    exit(ret)
