# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
store_collection = ops.get_collection_ref(_VARSTORE_KEY)
old = list(store_collection)
store_collection[:] = [store]
try:
    exit()
finally:
    store_collection[:] = old
