# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Internal-only entry point for `name_scope*`.

  Enters a compat.v1.name_scope only when in a function or graph,
  not when running fully eagerly.

  Args:
    name: The name argument that is passed to the op function.

  Returns:
    `name_scope*` context manager.
  """
if not context.executing_eagerly():
    exit(ops.name_scope_v1(name))
else:
    exit(NullContextmanager())
