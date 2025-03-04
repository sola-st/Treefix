# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Returns x + y element-wise.

  Example usages below.

  Add a scalar and a list:

  >>> x = [1, 2, 3, 4, 5]
  >>> y = 1
  >>> tf.add(x, y)
  <tf.Tensor: shape=(5,), dtype=int32, numpy=array([2, 3, 4, 5, 6],
  dtype=int32)>

  Note that binary `+` operator can be used instead:

  >>> x = tf.convert_to_tensor([1, 2, 3, 4, 5])
  >>> y = tf.convert_to_tensor(1)
  >>> x + y
  <tf.Tensor: shape=(5,), dtype=int32, numpy=array([2, 3, 4, 5, 6],
  dtype=int32)>

  Add a tensor and a list of same shape:

  >>> x = [1, 2, 3, 4, 5]
  >>> y = tf.constant([1, 2, 3, 4, 5])
  >>> tf.add(x, y)
  <tf.Tensor: shape=(5,), dtype=int32,
  numpy=array([ 2,  4,  6,  8, 10], dtype=int32)>

  **Warning**: If one of the inputs (`x` or `y`) is a tensor and the other is a
  non-tensor, the non-tensor input will adopt (or get casted to) the data type
  of the tensor input. This can potentially cause unwanted overflow or underflow
  conversion.

  For example,

  >>> x = tf.constant([1, 2], dtype=tf.int8)
  >>> y = [2**7 + 1, 2**7 + 2]
  >>> tf.add(x, y)
  <tf.Tensor: shape=(2,), dtype=int8, numpy=array([-126, -124], dtype=int8)>

  When adding two input values of different shapes, `Add` follows NumPy
  broadcasting rules. The two input array shapes are compared element-wise.
  Starting with the trailing dimensions, the two dimensions either have to be
  equal or one of them needs to be `1`.

  For example,

  >>> x = np.ones(6).reshape(1, 2, 1, 3)
  >>> y = np.ones(6).reshape(2, 1, 3, 1)
  >>> tf.add(x, y).shape.as_list()
  [2, 2, 3, 3]

  Another example with two arrays of different dimension.

  >>> x = np.ones([1, 2, 1, 4])
  >>> y = np.ones([3, 4])
  >>> tf.add(x, y).shape.as_list()
  [1, 2, 3, 4]

  The reduction version of this elementwise operation is `tf.math.reduce_sum`

  Args:
    x: A `tf.Tensor`. Must be one of the following types: bfloat16, half,
      float16, float32, float64, uint8, uint16, uint32, uint64, int8, int16,
      int32, int64, complex64, complex128, string.
    y: A `tf.Tensor`. Must have the same type as x.
    name: A name for the operation (optional)
  """
with ops.name_scope(name, "Add", [x]) as name:
    x = ops.convert_to_tensor(x, name="x")
    y = ops.convert_to_tensor(y, dtype_hint=x.dtype.base_dtype, name="y")
    if x.dtype == dtypes.string:
        exit(gen_math_ops.add(x, y, name=name))
    else:
        exit(gen_math_ops.add_v2(x, y, name=name))
