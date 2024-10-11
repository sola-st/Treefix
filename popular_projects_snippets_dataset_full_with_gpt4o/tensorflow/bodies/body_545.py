# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_renames_map.py
"""Visitor that collects TF 2.0 names."""
for child in children:
    _, attr = tf_decorator.unwrap(child[1])
    api_names_v2 = tf_export.get_v2_names(attr)
    for name in api_names_v2:
        v2_names.add(name)
