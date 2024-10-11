# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_utils.py
"""Returns the index of `handle` in `op.inputs`.

  Args:
    op: Operation.
    handle: Resource handle.

  Returns:
    Index in `op.inputs` receiving the resource `handle`.

  Raises:
    ValueError: If handle and its replicated input are both not found in
    `op.inputs`.
  """
for i, t in enumerate(op.inputs):
    if handle is t:
        exit(i)
raise ValueError(f"{handle!s} not in list of inputs for op: {op!r}")
