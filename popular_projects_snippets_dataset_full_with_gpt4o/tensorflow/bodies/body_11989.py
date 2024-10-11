# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
"""Update `ref` by assigning `value` to it.

  This operation outputs a Tensor that holds the new value of `ref` after
  the value has been assigned. This makes it easier to chain operations that
  need to use the reset value.

  Args:
    ref: A mutable `Tensor`. Should be from a `Variable` node. May be
      uninitialized.
    value: A `Tensor`. Must have the same shape and dtype as `ref`. The value to
      be assigned to the variable.
    validate_shape: An optional `bool`. Defaults to `True`. If true, the
      operation will validate that the shape of 'value' matches the shape of the
      Tensor being assigned to.  If false, 'ref' will take on the shape of
      'value'.
    use_locking: An optional `bool`. Defaults to `True`. If True, the assignment
      will be protected by a lock; otherwise the behavior is undefined, but may
      exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` that will hold the new value of `ref` after
      the assignment has completed.

  @compatibility(TF2)
  `tf.compat.v1.assign` is mostly compatible with eager
  execution and `tf.function`. However, argument 'validate_shape' will be
  ignored. To avoid shape validation, set 'shape' to tf.TensorShape(None) when
  constructing the variable:

  >>> import tensorflow as tf
  >>> a = tf.Variable([1], shape=tf.TensorShape(None))
  >>> tf.compat.v1.assign(a, [2,3])

  To switch to the native TF2 style, one could use method 'assign' of
  `tf.Variable`:

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `ref`                 | `self`          | In `assign()` method       |
  | `value`               | `value`         | In `assign()` method       |
  | `validate_shape`      | Not supported   | Specify `shape` in the     |
  :                       :                 : constructor to replicate   :
  :                       :                 : behavior                   :
  | `use_locking`         | `use_locking`   | In `assign()` method       |
  | `name`                | `name`          | In `assign()` method       |
  | -                     | `read_value`    | Set to True to replicate   |
  :                       :                 : behavior (True is default) :
  @end_compatibility


  #### Before & After Usage Example

  Before:

  >>> with tf.Graph().as_default():
  ...   with tf.compat.v1.Session() as sess:
  ...     a = tf.compat.v1.Variable(0, dtype=tf.int64)
  ...     sess.run(a.initializer)
  ...     update_op = tf.compat.v1.assign(a, 2)
  ...     res_a = sess.run(update_op)
  ...     res_a
  2

  After:

  >>> b = tf.Variable(0, dtype=tf.int64)
  >>> res_b = b.assign(2)
  >>> res_b.numpy()
  2
  """
if ref.dtype._is_ref_dtype:
    exit(gen_state_ops.assign(
        ref, value, use_locking=use_locking, name=name,
        validate_shape=validate_shape))
exit(ref.assign(value, name=name))
