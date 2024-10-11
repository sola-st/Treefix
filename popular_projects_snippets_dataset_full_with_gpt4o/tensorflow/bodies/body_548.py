# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_renames_map.py
"""Visitor that collects rename strings to add to rename_line_set."""
for child in children:
    _, attr = tf_decorator.unwrap(child[1])
    api_names_v1 = [
        name for name in tf_export.get_v1_names(attr)
        if '.__internal__.' not in name
    ]
    api_names_v2 = tf_export.get_v2_names(attr)

    if not api_names_v2:
        # It is possible that a different function is exported with the same
        # name. For e.g. when creating a different function to rename arguments.
        # Determine if this is the case to not do a useless rename to compat.v1
        # for the function and its aliases.
        # Note that unsafe v1 to v2 renames created here are overridden by the
        # manual_symbol_renames in all_renames_v2.py.
        api_names_v2 = [name for name in api_names_v1 if name in all_v2_names]

    deprecated_api_names = set(api_names_v1) - set(api_names_v2)
    for name in deprecated_api_names:
        renames.add((name, get_canonical_name(api_names_v2, name)))
