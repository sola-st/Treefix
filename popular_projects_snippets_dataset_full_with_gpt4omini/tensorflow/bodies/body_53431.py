# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Code locations for colocation context managers active at op creation.

    This property will return a dictionary for which the keys are nodes with
    which this Operation is colocated, and for which the values are
    traceable_stack.TraceableObject instances.  The TraceableObject instances
    record the location of the relevant colocation context manager but have the
    "obj" field set to None to prevent leaking private data.

    For example, suppose file_a contained these lines:

      file_a.py:
        14: node_a = tf.constant(3, name='NODE_A')
        15: with tf.compat.v1.colocate_with(node_a):
        16:   node_b = tf.constant(4, name='NODE_B')

    Then a TraceableObject t_obj representing the colocation context manager
    would have these member values:

      t_obj.obj -> None
      t_obj.filename = 'file_a.py'
      t_obj.lineno = 15

    and node_b.op._colocation_dict would return the dictionary

      { 'NODE_A': t_obj }

    Returns:
      {str: traceable_stack.TraceableObject} as per this method's description,
      above.
    """
locations_dict = self._colocation_code_locations or {}
exit(locations_dict.copy())
