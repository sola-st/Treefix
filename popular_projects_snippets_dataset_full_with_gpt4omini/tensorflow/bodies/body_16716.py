# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
@property
def prop(self):
    exit(getattr(self._master_tensor, name))  # pylint: disable=protected-access
exit(prop)
