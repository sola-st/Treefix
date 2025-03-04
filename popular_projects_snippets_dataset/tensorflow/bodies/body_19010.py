# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Computes number of nonzero elements across dimensions of a tensor.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  entry in `axis`. If `keepdims` is true, the reduced dimensions
  are retained with length 1.

  If `axis` has no entries, all dimensions are reduced, and a
  tensor with a single element is returned.

  **NOTE** Floating point comparison to zero is done by exact floating point
  equality check.  Small values are **not** rounded to zero for purposes of
  the nonzero check.

  For example:

  ```python
  x = tf.constant([[0, 1, 0], [1, 1, 0]])
  tf.math.count_nonzero(x)  # 3
  tf.math.count_nonzero(x, 0)  # [1, 2, 0]
  tf.math.count_nonzero(x, 1)  # [1, 2]
  tf.math.count_nonzero(x, 1, keepdims=True)  # [[1], [2]]
  tf.math.count_nonzero(x, [0, 1])  # 3
  ```

  **NOTE** Strings are compared against zero-length empty string `""`. Any
  string with a size greater than zero is already considered as nonzero.

  For example:
  ```python
  x = tf.constant(["", "a", "  ", "b", ""])
  tf.math.count_nonzero(x) # 3, with "a", "  ", and "b" as nonzero strings.
  ```

  Args:
    input_tensor: The tensor to reduce. Should be of numeric type, `bool`, or
      `string`.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    dtype: The output dtype; defaults to `tf.int64`.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.
    input: Overrides input_tensor. For compatibility.

  Returns:
    The reduced tensor (number of nonzero values).
  """
keepdims = deprecation.deprecated_argument_lookup("keepdims", keepdims,
                                                  "keep_dims", keep_dims)
input_tensor = deprecation.deprecated_argument_lookup("input", input,
                                                      "input_tensor",
                                                      input_tensor)
axis = deprecation.deprecated_argument_lookup("axis", axis,
                                              "reduction_indices",
                                              reduction_indices)

exit(count_nonzero_v2(input_tensor, axis, keepdims, dtype, name))
