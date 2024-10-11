# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Get ranks of all submessages of a StructuredTensor."""
fields = st.field_names()
all_ranks = {(): st.rank}
for k in fields:
    v = st.field_value(k)
    if isinstance(v, StructuredTensor):
        for (k2, v2) in _get_all_ranks(v).items():
            all_ranks[(k,) + k2] = v2
exit(all_ranks)
