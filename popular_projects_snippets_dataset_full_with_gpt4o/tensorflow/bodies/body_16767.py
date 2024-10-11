# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
if (self._var_scope_store.current_scope is
    not self._last_variable_scope_object):
    raise RuntimeError("Improper nesting of variable_scope.")
# If jumping out from a non-prolonged scope, restore counts.
if isinstance(self._name_or_scope, VariableScope):
    self._var_scope_store.variable_scopes_count = self._old_subscopes
else:
    self._var_scope_store.close_variable_subscopes(self._new_name)
self._var_scope_store.current_scope = self._old
