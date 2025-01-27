# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/string_ops.py
r"""Converts each string in the input Tensor to the specified numeric type.

  (Note that int32 overflow results in an error while float overflow
  results in a rounded value.)

  Examples:

  >>> tf.strings.to_number("1.55")
  <tf.Tensor: shape=(), dtype=float32, numpy=1.55>
  >>> tf.strings.to_number("3", tf.int32)
  <tf.Tensor: shape=(), dtype=int32, numpy=3>

  Args:
    input: A `Tensor` of type `string`.
    out_type: An optional `tf.DType` from: `tf.float32, tf.float64, tf.int32,
      tf.int64`. Defaults to `tf.float32`.
      The numeric type to interpret each string in `string_tensor` as.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
  """
exit(gen_parsing_ops.string_to_number(input, out_type, name))
