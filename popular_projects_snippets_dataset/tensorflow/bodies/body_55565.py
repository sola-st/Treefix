# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Extracts `attr_protos`. For use in _apply_op_helper."""
for attr_def in op_def.attr:
    key = attr_def.name
    value = attrs[key]

    if attr_def.HasField("default_value") and value is None:
        attr_value = attr_value_pb2.AttrValue()
        attr_value.CopyFrom(attr_def.default_value)
        attr_protos[key] = attr_value
        continue

    attr_value = value_to_attr_value(value, attr_def.type, key)
    if attr_def.type.startswith("list("):
        _SatisfiesLengthConstraint(len(value), attr_def, key, op_type_name)
    if attr_def.HasField("allowed_values"):
        if attr_def.type == "string":
            _SatisfiesAllowedStringsConstraint(attr_value.s, attr_def, key,
                                               op_type_name)
        elif attr_def.type == "list(string)":
            for value in attr_value.list.s:
                _SatisfiesAllowedStringsConstraint(value, attr_def, key, op_type_name)
    if attr_def.has_minimum and attr_def.type == "int":
        _SatisfiesIntMinimumConstraint(attr_value.i, attr_def, key, op_type_name)
    if attr_def.type == "type":
        _SatisfiesTypeConstraint(attr_value.type, attr_def, key)
    if attr_def.type == "list(type)":
        for value in attr_value.list.type:
            _SatisfiesTypeConstraint(value, attr_def, key)

    attr_protos[key] = attr_value
