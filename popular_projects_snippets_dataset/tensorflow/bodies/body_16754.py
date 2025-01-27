# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
store = ops.get_collection(_VARSTORE_KEY)
if store:
    exit(store[0])
store = _VariableStore()
ops.add_to_collection(_VARSTORE_KEY, store)
exit(store)
