# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns the overall concatenated value as a `Tensor`.

    The returned tensor will not inherit the control dependencies from the scope
    where the value is used, which is similar to getting the value of
    `Variable`.

    Returns:
      `Tensor` containing the concatenated value.
    """
with ops.control_dependencies(None):
    exit(self._concat())
