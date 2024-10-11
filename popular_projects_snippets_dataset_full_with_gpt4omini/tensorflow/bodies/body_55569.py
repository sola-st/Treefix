# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Extracts the `default_type_attr_map` and `allowed_list_attr_map`."""
# TODO(b/31302892): Currently the defaults don't work in the right
# way if you have two inputs, one of whose type resolution depends
# on the other.  Handling this will require restructuring this code
# significantly.
for attr_def in op_def.attr:
    if attr_def.type != "type":
        continue
    key = attr_def.name
    if attr_def.HasField("default_value"):
        default_type_attr_map[key] = dtypes.as_dtype(
            attr_def.default_value.type)
    if attr_def.HasField("allowed_values"):
        allowed_list_attr_map[key] = attr_def.allowed_values.list.type
