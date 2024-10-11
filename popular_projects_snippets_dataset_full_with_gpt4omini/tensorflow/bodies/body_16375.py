# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
self._variable_scope_name = variable_scope_name
default = variable_scope._get_default_variable_store()  # pylint: disable=protected-access
if default._store_eager_variables:  # pylint: disable=protected-access
    self._eager_variable_store = variable_scope.EagerVariableStore(default)
else:
    # If no outer eager variable store has been made,
    # the template needs to create one
    self._eager_variable_store = variable_scope.EagerVariableStore()
self._used_once = False
