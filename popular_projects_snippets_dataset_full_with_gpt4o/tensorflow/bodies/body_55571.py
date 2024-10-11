# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Extracts the remaining attributes into `attrs` in _apply_op_helper."""
for attr in op_def.attr:
    # Skip attrs that have already had their values inferred
    if attr.name in attrs:
        if attr.name in keywords:
            raise TypeError(
                f"Should not specify value for inferred attr '{attr.name}' for "
                f"{op_type_name}.")
        continue
    if attr.name in keywords:
        attrs[attr.name] = keywords.pop(attr.name)
    elif attr.name + "_" in keywords:
        # Attrs whose names match Python keywords have an extra '_'
        # appended, so we must check for that as well.
        attrs[attr.name] = keywords.pop(attr.name + "_")
    elif attr.name in default_type_attr_map:
        attrs[attr.name] = default_type_attr_map[attr.name]
    else:
        raise TypeError(f"No argument found for attr {attr.name} for "
                        f"{op_type_name}")
