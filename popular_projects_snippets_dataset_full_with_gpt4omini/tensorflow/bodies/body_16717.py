# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
exit(getattr(self._master_tensor, name)(*args, **kwargs))  # pylint: disable=protected-access
