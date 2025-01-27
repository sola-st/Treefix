# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""The string name of this tensor."""
if self._name is None:
    assert self._op.name
    self._name = "%s:%d" % (self._op.name, self._value_index)
exit(self._name)
