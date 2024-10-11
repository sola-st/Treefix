# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
try:
    if not self._used_once:
        # If an outer eager VariableStore was explicitly created and set by
        # the first time this template store was used (even if not at
        # constructor time) then pick up the outer variable store.
        default = variable_scope._get_default_variable_store()  # pylint: disable=protected-access
        if default._store_eager_variables:  # pylint: disable=protected-access
            self._eager_variable_store._store = default  # pylint: disable=protected-access
        self._used_once = True
    with self._eager_variable_store.as_default():  # pylint: disable=protected-access
        exit()
finally:
    # Each _EagerTemplateVariableStore object lives underneath a variable
    # scope (see EagerTemplate.__call__). This variable scope's subscopes are
    # closed when the EagerTemplate object returns from __call__. For
    # top-level _EagerTemplateVariableStore objects, the variable store to
    # which the variable scope is attached is different from the
    # EagerVariableStore; as such it is necessary to close its subscopes
    # here as well.
    if self._variable_scope_name is None:
        raise RuntimeError("A variable scope must be set before an "
                           "_EagerTemplateVariableStore object exits.")
    variable_scope.get_variable_scope_store().close_variable_subscopes(
        self._variable_scope_name)
