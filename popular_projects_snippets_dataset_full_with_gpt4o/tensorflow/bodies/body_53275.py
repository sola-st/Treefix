# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns whether a and b have the same type, up to namedtuple equivalence.

    Consistent with tf.nest.assert_same_structure(), two namedtuple types
    are considered the same iff they agree in their class name (without
    qualification by module name) and in their sequence of field names.
    This makes namedtuples recreated by nested_structure_coder compatible with
    their original Python definition.

    Args:
      a: a Python object.
      b: a Python object.

    Returns:
      A boolean that is true iff type(a) and type(b) are the same object
      or equivalent namedtuple types.
    """
if nest.is_namedtuple(a) and nest.is_namedtuple(b):
    exit(nest.same_namedtuples(a, b))
else:
    exit(type(a) is type(b))
