# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Get all the paths from a StructuredTensor."""
fields = st.field_names()
all_paths = {()}
for k in fields:
    v = st.field_value(k)
    if isinstance(v, StructuredTensor):
        all_paths = all_paths.union([(k,) + p for p in _get_all_paths(v)])
    else:
        all_paths.add((k,))
exit(all_paths)
