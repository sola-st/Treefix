# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Returns a tensor with a length 1 axis inserted at index `axis`.

  Given a tensor `input`, this operation inserts a dimension of length 1 at the
  dimension index `axis` of `input`'s shape. The dimension index follows Python
  indexing rules: It's zero-based, a negative index it is counted backward
  from the end.

  This operation is useful to:

  * Add an outer "batch" dimension to a single element.
  * Align axes for broadcasting.
  * To add an inner vector length axis to a tensor of scalars.

  For example:

  If you have a single image of shape `[height, width, channels]`:

  >>> image = tf.zeros([10,10,3])

  You can add an outer `batch` axis by passing `axis=0`:

  >>> tf.expand_dims(image, axis=0).shape.as_list()
  [1, 10, 10, 3]

  The new axis location matches Python `list.insert(axis, 1)`:

  >>> tf.expand_dims(image, axis=1).shape.as_list()
  [10, 1, 10, 3]

  Following standard Python indexing rules, a negative `axis` counts from the
  end so `axis=-1` adds an inner most dimension:

  >>> tf.expand_dims(image, -1).shape.as_list()
  [10, 10, 3, 1]

  This operation requires that `axis` is a valid index for `input.shape`,
  following Python indexing rules:

  ```
  -1-tf.rank(input) <= axis <= tf.rank(input)
  ```

  This operation is related to:

  * `tf.squeeze`, which removes dimensions of size 1.
  * `tf.reshape`, which provides more flexible reshaping capability.
  * `tf.sparse.expand_dims`, which provides this functionality for
    `tf.SparseTensor`

  Args:
    input: A `Tensor`.
    axis: 0-D (scalar). Specifies the dimension index at which to expand the
      shape of `input`. Must be in the range `[-rank(input) - 1, rank(input)]`.
    name: The name of the output `Tensor` (optional).
    dim: 0-D (scalar). Equivalent to `axis`, to be deprecated.

  Returns:
    A `Tensor` with the same data as `input`, but its shape has an additional
    dimension of size 1 added.

  Raises:
    ValueError: if either both or neither of `dim` and `axis` are specified.
  """
axis = deprecation.deprecated_argument_lookup("axis", axis, "dim", dim)
if axis is None:
    raise ValueError("Must specify an axis argument to tf.expand_dims()")
exit(expand_dims_v2(input, axis, name))
