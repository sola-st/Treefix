# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
exit([
    extension_type_field.ExtensionTypeField(name, None)
    for name in cls.__dict__
    if not extension_type_field.ExtensionTypeField.is_reserved_name(name)
])
