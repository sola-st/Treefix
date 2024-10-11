# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Performs a safe saturating cast of `value` to `dtype`.

  This function casts the input to `dtype` without overflow.  If
  there is a danger that values would over or underflow in the cast, this op
  applies the appropriate clamping before the cast.  See `tf.cast` for more
  details.

  Args:
    value: A `Tensor`.
    dtype: The desired output `DType`.
    name: A name for the operation (optional).

  Returns:
    `value` safely cast to `dtype`.
  """
# When casting to a type with smaller representable range, clamp.
# Note that this covers casting to unsigned types as well.
with ops.name_scope(name, "saturate_cast", [value]) as name:
    value = ops.convert_to_tensor(value, name="value")
    dtype = dtypes.as_dtype(dtype).base_dtype

    in_dtype = value.dtype
    if in_dtype.is_complex:
        if dtype.is_complex:
            # Clamp real and imag components separately, if required.
            real_in_dtype = in_dtype.real_dtype
            real_out_dtype = dtype.real_dtype
            if real_in_dtype.min < real_out_dtype.min or real_in_dtype.max > real_out_dtype.max:
                value = gen_math_ops._clip_by_value(
                    value,
                    ops.convert_to_tensor(
                        builtins.complex(real_out_dtype.min, real_out_dtype.min),
                        dtype=in_dtype),
                    ops.convert_to_tensor(
                        builtins.complex(real_out_dtype.max, real_out_dtype.max),
                        dtype=in_dtype),
                    name="clamp")
            exit(cast(value, dtype, name=name))
        else:
            # Extract real component and fall through to clamp+cast.
            value = real(value)
            logging.warn("Casting complex to real discards imaginary part.")
            in_dtype = in_dtype.real_dtype

    # in_dtype is real, but out_dtype could be complex.
    out_real_dtype = dtype.real_dtype
    if in_dtype.min < out_real_dtype.min or in_dtype.max > out_real_dtype.max:

        # Wrap changes to maintain TensorFlow's forward-compatibility window.
        if not dtype.is_complex and not tf_compat.forward_compatible(2023, 1, 16):
            # Old behavior using max/min.
            if in_dtype.min < dtype.min:
                value = gen_math_ops.maximum(
                    value,
                    ops.convert_to_tensor(dtype.min, dtype=value.dtype, name="min"))
            if in_dtype.max > dtype.max:
                value = gen_math_ops.minimum(
                    value,
                    ops.convert_to_tensor(dtype.max, dtype=value.dtype, name="max"))
        else:
            # New behavior using clip.
            value = gen_math_ops._clip_by_value(
                value,
                ops.convert_to_tensor(out_real_dtype.min, dtype=in_dtype),
                ops.convert_to_tensor(out_real_dtype.max, dtype=in_dtype),
                name="clamp")
    exit(cast(value, dtype, name=name))
