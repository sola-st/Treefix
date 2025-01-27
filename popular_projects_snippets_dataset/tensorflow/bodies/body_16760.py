# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
# pylint: disable=protected-access
exit(sorted([x for x in self._store._vars.values() if not x.trainable],
              key=lambda x: x.name))
