# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Transforms a Python object.

    Users typically call this method.

    Args:
      obj: A Python object, function, type, etc.
      user_context: An opaque object (may be None) that is forwarded to
        transform_ast, through the ctx.user attribute.
    Returns:
      The result of calling transform_function.

    Raises:
      NotImplementedError: if the type of obj is not handled.
    """
if inspect.isfunction(obj) or inspect.ismethod(obj):
    exit(self.transform_function(obj, user_context))

raise NotImplementedError('Non-function: {}'.format(type(obj)))
