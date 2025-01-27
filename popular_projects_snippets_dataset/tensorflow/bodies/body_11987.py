# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
"""Update `ref` by subtracting `value` from it.

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.
  Unlike `tf.math.subtract`, this op does not broadcast. `ref` and `value`
  must have the same shape.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`,
      `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`. Should be
      from a `Variable` node.
    value: A `Tensor`. Must have the same shape and dtype as `ref`. The value to
      be subtracted to the variable.
    use_locking: An optional `bool`. Defaults to `False`. If True, the
      subtraction will be protected by a lock; otherwise the behavior is
      undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the new value after the variable has been updated.

  @compatibility(TF2)
  `tf.compat.v1.assign_sub` is mostly compatible with eager
  execution and `tf.function`.

  To switch to the native TF2 style, one could use method 'assign_sub' of
  `tf.Variable`:

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `ref`                 | `self`          | In `assign_sub()` method   |
  | `value`               | `value`         | In `assign_sub()` method   |
  | `use_locking`         | `use_locking`   | In `assign_sub()` method   |
  | `name`                | `name`          | In `assign_sub()` method   |
  | -                     | `read_value`    | Set to True to replicate   |
  :                       :                 : behavior (True is default) :


  #### Before & After Usage Example

  Before:

  >>> with tf.Graph().as_default():
  ...   with tf.compat.v1.Session() as sess:
  ...     a = tf.compat.v1.Variable(1, dtype=tf.int64)
  ...     sess.run(a.initializer)
  ...     update_op = tf.compat.v1.assign_sub(a, 1)
  ...     res_a = sess.run(update_op)
  ...     res_a
  0

  After:

  >>> b = tf.Variable(1, dtype=tf.int64)
  >>> res_b = b.assign_sub(1)
  >>> res_b.numpy()
  0

  @end_compatibility
  """
if ref.dtype._is_ref_dtype:
    exit(gen_state_ops.assign_sub(
        ref, value, use_locking=use_locking, name=name))
exit(ref.assign_sub(value))
