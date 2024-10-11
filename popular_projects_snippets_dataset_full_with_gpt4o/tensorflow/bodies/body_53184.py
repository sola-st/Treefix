# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
state = _change_nested_mappings_to(state, immutable_dict.ImmutableDict)
exit(_create_object_from_type_and_dict(cls, state))
