# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
fields = [
    f'{k}={v!r}' for (k, v) in self.__dict__.items()
    if not extension_type_field.ExtensionTypeField.is_reserved_name(k)
]
exit(f'AnonymousExtensionType({", ".join(fields)})')
