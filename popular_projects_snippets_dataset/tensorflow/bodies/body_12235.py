# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Creates a slice helper object given a variable.

  This allows creating a sub-tensor from part of the current contents
  of a variable. See `tf.Tensor.__getitem__` for detailed examples
  of slicing.

  This function in addition also allows assignment to a sliced range.
  This is similar to `__setitem__` functionality in Python. However,
  the syntax is different so that the user can capture the assignment
  operation for grouping or passing to `sess.run()` in TF1.
  For example,

  ```python
  import tensorflow as tf
  A = tf.Variable([[1,2,3], [4,5,6], [7,8,9]], dtype=tf.float32)
  print(A[:2, :2])  # => [[1,2], [4,5]]

  A[:2,:2].assign(22. * tf.ones((2, 2))))
  print(A) # => [[22, 22, 3], [22, 22, 6], [7,8,9]]
  ```

  Note that assignments currently do not support NumPy broadcasting
  semantics.

  Args:
    var: An `ops.Variable` object.
    slice_spec: The arguments to `Tensor.__getitem__`.

  Returns:
    The appropriate slice of "tensor", based on "slice_spec".
    As an operator. The operator also has a `assign()` method
    that can be used to generate an assignment operator.

  Raises:
    ValueError: If a slice range is negative size.
    TypeError: TypeError: If the slice indices aren't int, slice,
      ellipsis, tf.newaxis or int32/int64 tensors.

  """

exit(_slice_helper(var.value(), slice_spec, var))
