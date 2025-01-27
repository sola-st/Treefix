# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Get this scope's variables."""
scope = self._name + "/" if self._name else ""
exit(ops.get_collection(name, scope))
