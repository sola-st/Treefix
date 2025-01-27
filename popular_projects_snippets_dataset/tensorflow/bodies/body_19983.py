# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/bfloat16.py
"""Scope class for bfloat16 variables so that the model uses custom getter.

  This enables variables to be read as bfloat16 type when using get_variable.

  Arguments:
    name: Name to use for scope.

  Yields:
    a variable scope.
  """
if name is None:
    name = ''
with variable_scope.variable_scope(
    name, custom_getter=_get_custom_getter()) as varscope:
    exit(varscope)
