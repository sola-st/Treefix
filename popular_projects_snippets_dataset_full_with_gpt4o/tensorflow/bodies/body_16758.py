# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
exit(sorted(self._store._vars.values(), key=lambda x: x.name))  # pylint: disable=protected-access
