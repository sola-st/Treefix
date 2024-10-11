# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
if store is not None:
    if not store._store_eager_variables:  # pylint: disable=protected-access
        raise ValueError("Cannot construct EagerVariableStore from a "
                         "VariableStore object that does not hold eager "
                         "variables.")
    self._store = store
else:
    self._store = _VariableStore()
self._store._store_eager_variables = True  # pylint: disable=protected-access
