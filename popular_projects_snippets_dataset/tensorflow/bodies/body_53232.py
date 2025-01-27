# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
exit(tuple(
    (name, _change_nested_mappings_to(value, dict))
    for (name, value) in self.__dict__.items()
    if not extension_type_field.ExtensionTypeField.is_reserved_name(name)))
