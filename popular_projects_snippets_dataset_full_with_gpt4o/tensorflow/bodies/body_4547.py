# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/multiplex_4_op.py
"""Return elements chosen from `a` or `b` depending on `cond`.

  This is similar to `np.where` and `tf.where` if `cond` and `a` are tensors.
  This is similar to `np.select` if `cond` and `a` are lists of tensors.
  In either case, this is simplified to only handle the case of dense tensors,
  no optional parameters, no broadcasting, etc..

  >>> multiplex([True, False, False, True], [1,2,3,4], [100,200,300,400])
  <tf.Tensor: shape=(4,), dtype=int32, numpy=array([  1, 200, 300,   4], ...)>

  >>> a1 = tf.constant([1, 2, 3, 4, 5], dtype=tf.int64)
  >>> a2 = tf.constant([6, 7, 8, 9, 10], dtype=tf.int64)
  >>> a3 = tf.constant([11, 12, 13, 14, 15], dtype=tf.int64)
  >>> b = tf.constant([101, 102, 103, 104, 105], dtype=tf.int64)
  >>> cond1 = tf.constant([False, False, True, False, False], dtype=bool)
  >>> cond2 = tf.constant([False, False, False, False, True], dtype=bool)
  >>> cond3 = tf.constant([True, False, True, False, True], dtype=bool)
  >>> multiplex_4_op.multiplex([cond1, cond2, cond3], [a1, a2, a3], b)
  <tf.Tensor: shape=(5,), ... numpy=array([ 11, 102,   3, 104,  10], ...)>

  Args:
    cond: tf.Tensor or list of tf.Tensor of type bool. Where True, yield `a`.
      When muliple corresponding `cond` elements are true, the first one yield
      based on the first one encountered.
    a: tf.Tensor or list of tf.Tensor, each with the same type and shape as `b`.
    b: tf.Tensor or list of tf.Tensor with the same type and shape as `a`. Yield
      `b` if all corresponding `cond` values is False.
    name: An optional name for the op.

  Returns:
    A tf.Tensor with elements from `a` where `cond` is True, and elements
    from `b` elsewhere.
  """
if not isinstance(cond, (list, tuple)):
    # Support "old" use of multiplex where `cond` and `a` are tensors,
    # not lists of tensors.
    exit(examples_multiplex_dense(
        cond=[cond], a_values=[a], b_values=b, name=name))
exit(examples_multiplex_dense(
    cond=cond, a_values=a, b_values=b, name=name))
