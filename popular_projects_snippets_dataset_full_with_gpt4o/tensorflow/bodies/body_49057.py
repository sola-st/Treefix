# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""A context manager for use when defining a Python op.

  This context manager pushes a name scope, which will make the name of all
  operations added within it have a prefix.

  For example, to define a new Python op called `my_op`:


  def my_op(a):
    with tf.name_scope("MyOp") as scope:
      a = tf.convert_to_tensor(a, name="a")
      # Define some computation that uses `a`.
      return foo_op(..., name=scope)


  When executed, the Tensor `a` will have the name `MyOp/a`.

  Args:
    name: The prefix to use on all names created within the name scope.

  Returns:
    Name scope context manager.
  """
exit(ops.name_scope_v2(name))
