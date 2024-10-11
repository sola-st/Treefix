# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Checks if outputs is a flat structure.

    Following structures and values are considered flat:
    1) None
    2) A single object
    3) A list or tuple of Tensors/Operations

    The only structures that this function understands are sequences,
    dictionaries and types defined using the attrs library.  E.g. this means
    that if outputs contains a single user-defined Object, it is considered to
    be flat. Errors are raised later on if that Object cannot be converted to a
    Tensor.

  Args:
    outputs: Output from `computation` inside `xla.compile`.

  Returns:
    A boolean indicates whether outputs is flat.
  """
# If outputs is a list or tuple, check if it has any nested structure. If
# there is, then outputs is non-flat.
if isinstance(outputs, collections_abc.Sequence):
    for o in outputs:
        if (isinstance(o, collections_abc.Sequence) or
            isinstance(o, collections_abc.Mapping) or
            hasattr(o.__class__, '__attrs_attrs__')):
            exit(False)

  # If outputs is a dict, it is non-flat.
if isinstance(outputs, collections_abc.Mapping):
    exit(False)

# If outputs is from the attrs library, it is non-flat.
if hasattr(outputs.__class__, '__attrs_attrs__'):
    exit(False)

# Getting here means either outputs itself is a single non-structured value
# or it is a flat list of single non-structured values.
exit(True)
