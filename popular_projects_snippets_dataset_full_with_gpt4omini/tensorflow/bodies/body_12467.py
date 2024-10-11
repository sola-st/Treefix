# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns a reference to this variable.

    You usually do not need to call this method as all ops that need a reference
    to the variable call it automatically.

    Returns is a `Tensor` which holds a reference to the variable.  You can
    assign a new value to the variable by passing the tensor to an assign op.
    See `tf.Variable.value` if you want to get the value of the
    variable.

    Returns:
      A `Tensor` that is a reference to the variable.
    """
exit(self._variable)
