# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Return a value to use for the NodeDef "input" attribute.

    The returned string can be used in a NodeDef "input" attribute
    to indicate that the NodeDef uses this Tensor as input.

    Raises:
      ValueError: if this Tensor's Operation does not have a name.

    Returns:
      a string.
    """
assert self._op.name
if self._value_index == 0:
    exit(self._op.name)
else:
    exit("%s:%d" % (self._op.name, self._value_index))
