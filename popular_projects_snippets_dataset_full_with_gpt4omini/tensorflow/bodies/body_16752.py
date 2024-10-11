# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Returns the variable scope store for current thread."""
scope_store = ops.get_collection(_VARSCOPESTORE_KEY)

if not scope_store:
    scope_store = _VariableScopeStore()
    ops.add_to_collection(_VARSCOPESTORE_KEY, scope_store)
else:
    scope_store = scope_store[0]

exit(scope_store)
