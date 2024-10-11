# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Convert `image` to `dtype`, scaling its values if needed.

  The operation supports data types (for `image` and `dtype`) of
  `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`,
  `float16`, `float32`, `float64`, `bfloat16`.

  Images that are represented using floating point values are expected to have
  values in the range [0,1). Image data stored in integer data types are
  expected to have values in the range `[0,MAX]`, where `MAX` is the largest
  positive representable number for the data type.

  This op converts between data types, scaling the values appropriately before
  casting.

  Usage Example:

  >>> x = [[[1, 2, 3], [4, 5, 6]],
  ...      [[7, 8, 9], [10, 11, 12]]]
  >>> x_int8 = tf.convert_to_tensor(x, dtype=tf.int8)
  >>> tf.image.convert_image_dtype(x_int8, dtype=tf.float16, saturate=False)
  <tf.Tensor: shape=(2, 2, 3), dtype=float16, numpy=
  array([[[0.00787, 0.01575, 0.02362],
          [0.0315 , 0.03937, 0.04724]],
         [[0.0551 , 0.063  , 0.07086],
          [0.07874, 0.0866 , 0.0945 ]]], dtype=float16)>

  Converting integer types to floating point types returns normalized floating
  point values in the range [0, 1); the values are normalized by the `MAX` value
  of the input dtype. Consider the following two examples:

  >>> a = [[[1], [2]], [[3], [4]]]
  >>> a_int8 = tf.convert_to_tensor(a, dtype=tf.int8)
  >>> tf.image.convert_image_dtype(a_int8, dtype=tf.float32)
  <tf.Tensor: shape=(2, 2, 1), dtype=float32, numpy=
  array([[[0.00787402],
          [0.01574803]],
         [[0.02362205],
          [0.03149606]]], dtype=float32)>

  >>> a_int32 = tf.convert_to_tensor(a, dtype=tf.int32)
  >>> tf.image.convert_image_dtype(a_int32, dtype=tf.float32)
  <tf.Tensor: shape=(2, 2, 1), dtype=float32, numpy=
  array([[[4.6566129e-10],
          [9.3132257e-10]],
         [[1.3969839e-09],
          [1.8626451e-09]]], dtype=float32)>

  Despite having identical values of `a` and output dtype of `float32`, the
  outputs differ due to the different input dtypes (`int8` vs. `int32`). This
  is, again, because the values are normalized by the `MAX` value of the input
  dtype.

  Note that converting floating point values to integer type may lose precision.
  In the example below, an image tensor `b` of dtype `float32` is converted to
  `int8` and back to `float32`. The final output, however, is different from
  the original input `b` due to precision loss.

  >>> b = [[[0.12], [0.34]], [[0.56], [0.78]]]
  >>> b_float32 = tf.convert_to_tensor(b, dtype=tf.float32)
  >>> b_int8 = tf.image.convert_image_dtype(b_float32, dtype=tf.int8)
  >>> tf.image.convert_image_dtype(b_int8, dtype=tf.float32)
  <tf.Tensor: shape=(2, 2, 1), dtype=float32, numpy=
  array([[[0.11811024],
          [0.33858266]],
         [[0.5590551 ],
          [0.77952754]]], dtype=float32)>

  Scaling up from an integer type (input dtype) to another integer type (output
  dtype) will not map input dtype's `MAX` to output dtype's `MAX` but converting
  back and forth should result in no change. For example, as shown below, the
  `MAX` value of int8 (=127) is not mapped to the `MAX` value of int16 (=32,767)
  but, when scaled back, we get the same, original values of `c`.

  >>> c = [[[1], [2]], [[127], [127]]]
  >>> c_int8 = tf.convert_to_tensor(c, dtype=tf.int8)
  >>> c_int16 = tf.image.convert_image_dtype(c_int8, dtype=tf.int16)
  >>> print(c_int16)
  tf.Tensor(
  [[[  256]
    [  512]]
   [[32512]
    [32512]]], shape=(2, 2, 1), dtype=int16)
  >>> c_int8_back = tf.image.convert_image_dtype(c_int16, dtype=tf.int8)
  >>> print(c_int8_back)
  tf.Tensor(
  [[[  1]
    [  2]]
   [[127]
    [127]]], shape=(2, 2, 1), dtype=int8)

  Scaling down from an integer type to another integer type can be a lossy
  conversion. Notice in the example below that converting `int16` to `uint8` and
  back to `int16` has lost precision.

  >>> d = [[[1000], [2000]], [[3000], [4000]]]
  >>> d_int16 = tf.convert_to_tensor(d, dtype=tf.int16)
  >>> d_uint8 = tf.image.convert_image_dtype(d_int16, dtype=tf.uint8)
  >>> d_int16_back = tf.image.convert_image_dtype(d_uint8, dtype=tf.int16)
  >>> print(d_int16_back)
  tf.Tensor(
  [[[ 896]
    [1920]]
   [[2944]
    [3968]]], shape=(2, 2, 1), dtype=int16)

  Note that converting from floating point inputs to integer types may lead to
  over/underflow problems. Set saturate to `True` to avoid such problem in
  problematic conversions. If enabled, saturation will clip the output into the
  allowed range before performing a potentially dangerous cast (and only before
  performing such a cast, i.e., when casting from a floating point to an integer
  type, and when casting from a signed to an unsigned type; `saturate` has no
  effect on casts between floats, or on casts that increase the type's range).

  Args:
    image: An image.
    dtype: A `DType` to convert `image` to.
    saturate: If `True`, clip the input before casting (if necessary).
    name: A name for this operation (optional).

  Returns:
    `image`, converted to `dtype`.

  Raises:
    AttributeError: Raises an attribute error when dtype is neither
    float nor integer.
  """
image = ops.convert_to_tensor(image, name='image')
dtype = dtypes.as_dtype(dtype)
if not dtype.is_floating and not dtype.is_integer:
    raise AttributeError('dtype must be either floating point or integer')
if dtype == image.dtype:
    exit(array_ops.identity(image, name=name))

with ops.name_scope(name, 'convert_image', [image]) as name:
    # Both integer: use integer multiplication in the larger range
    if image.dtype.is_integer and dtype.is_integer:
        scale_in = image.dtype.max
        scale_out = dtype.max
        if scale_in > scale_out:
            # Scaling down, scale first, then cast. The scaling factor will
            # cause in.max to be mapped to above out.max but below out.max+1,
            # so that the output is safely in the supported range.
            scale = (scale_in + 1) // (scale_out + 1)
            scaled = math_ops.floordiv(image, scale)

            if saturate:
                exit(math_ops.saturate_cast(scaled, dtype, name=name))
            else:
                exit(math_ops.cast(scaled, dtype, name=name))
        else:
            # Scaling up, cast first, then scale. The scale will not map in.max to
            # out.max, but converting back and forth should result in no change.
            if saturate:
                cast = math_ops.saturate_cast(image, dtype)
            else:
                cast = math_ops.cast(image, dtype)
            scale = (scale_out + 1) // (scale_in + 1)
            exit(math_ops.multiply(cast, scale, name=name))
    elif image.dtype.is_floating and dtype.is_floating:
        # Both float: Just cast, no possible overflows in the allowed ranges.
        # Note: We're ignoring float overflows. If your image dynamic range
        # exceeds float range, you're on your own.
        exit(math_ops.cast(image, dtype, name=name))
    else:
        if image.dtype.is_integer:
            # Converting to float: first cast, then scale. No saturation possible.
            cast = math_ops.cast(image, dtype)
            scale = 1. / image.dtype.max
            exit(math_ops.multiply(cast, scale, name=name))
        else:
            # Converting from float: first scale, then cast
            scale = dtype.max + 0.5  # avoid rounding problems in the cast
            scaled = math_ops.multiply(image, scale)
            if saturate:
                exit(math_ops.saturate_cast(scaled, dtype, name=name))
            else:
                exit(math_ops.cast(scaled, dtype, name=name))
