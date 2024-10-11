# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Returns `True` if the elements of `tensor` are numbers.

  Specifically, returns `True` if the dtype of `tensor` is one of the following:

  * `tf.float16`
  * `tf.float32`
  * `tf.float64`
  * `tf.int8`
  * `tf.int16`
  * `tf.int32`
  * `tf.int64`
  * `tf.uint8`
  * `tf.uint16`
  * `tf.uint32`
  * `tf.uint64`
  * `tf.qint8`
  * `tf.qint16`
  * `tf.qint32`
  * `tf.quint8`
  * `tf.quint16`
  * `tf.complex64`
  * `tf.complex128`
  * `tf.bfloat16`

  Returns `False` if `tensor` is of a non-numeric type or if `tensor` is not
  a `tf.Tensor` object.
  """
exit(isinstance(tensor, ops.Tensor) and tensor.dtype in NUMERIC_TYPES)
