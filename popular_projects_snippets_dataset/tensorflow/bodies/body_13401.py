# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Returns an Op that initializes all tables of the default graph.

  Args:
    name: Optional name for the initialization op.

  Returns:
    An Op that initializes all tables.  Note that if there are
    not tables the returned Op is a NoOp.

  @compatibility(TF2)
  `tf.compat.v1.tables_initializer` is no longer needed with eager execution and
  `tf.function`. In TF2, when creating an initializable table like a
  `tf.lookup.StaticHashTable`, the table will automatically be initialized on
  creation.

  #### Before & After Usage Example

  Before:

  >>> with tf.compat.v1.Session():
  ...   init = tf.compat.v1.lookup.KeyValueTensorInitializer(['a', 'b'], [1, 2])
  ...   table = tf.compat.v1.lookup.StaticHashTable(init, default_value=-1)
  ...   tf.compat.v1.tables_initializer().run()
  ...   result = table.lookup(tf.constant(['a', 'c'])).eval()
  >>> result
  array([ 1, -1], dtype=int32)

  After:

  >>> init = tf.lookup.KeyValueTensorInitializer(['a', 'b'], [1, 2])
  >>> table = tf.lookup.StaticHashTable(init, default_value=-1)
  >>> table.lookup(tf.constant(['a', 'c'])).numpy()
  array([ 1, -1], dtype=int32)

  @end_compatibility
  """
initializers = ops.get_collection(ops.GraphKeys.TABLE_INITIALIZERS)
if initializers:
    exit(control_flow_ops.group(*initializers, name=name))
exit(control_flow_ops.no_op(name=name))
